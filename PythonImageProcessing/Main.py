# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:13:38 2017

@author: Bedirhan
"""

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from skimage import io
import io as IO
import sys
import matplotlib.pyplot as plt
from scipy import ndimage
import scipy
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
import matplotlib.widgets as widgets
import matplotlib.image as mimg
import cv2
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb
from skimage import color
import matplotlib.patches as mpatches
import DataBase
import os
import base64
import math
import FaceDetection

from tasarim import Ui_Dialog

class MainWindow(QtGui.QMainWindow,Ui_Dialog):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.t2_cb_mantiksal.currentIndexChanged.connect(self.mantiksal_combobox)
        self.t3_cb_shapes.currentIndexChanged.connect(self.labeling_combobox)
        self.slider_gurultu.valueChanged.connect(self.slider_value_changed)
        self.t1_hs_rotate.valueChanged.connect(self.rotate_img)
        self.gb_main_menu.setGeometry(QtCore.QRect(0, 48, 0, 0))
        self.pb_main_menu.clicked.connect(self.main_menu_clicked)
        self.gb_menu.setGeometry(QtCore.QRect(10, 70, 0, 0))
        self.sifirla()
        self.t1_pb_menu.clicked.connect(self.menu_clicked)
        self.pb_menu_1.clicked.connect(self.mm_temel_islemler)
        self.pb_menu_2.clicked.connect(self.mm_mantiksal_islemler)
        self.pb_menu_3.clicked.connect(self.mm_etiketleme)
        self.pb_menu_4.clicked.connect(self.mm_gurultu_olusturma)
        self.pb_menu_5.clicked.connect(self.mm_erosion)
        self.pb_menu_6.clicked.connect(self.mm_template)
        self.pb_menu_7.clicked.connect(self.mm_face_detection)
        self.DBConnect=DataBase.connect("root","","localhost","goruntu_isleme")
        self.cursor=self.DBConnect.cursor(buffered=True)
        self.pb_exit.clicked.connect(self.shutdown)
        self.t3_pb_tahmin.clicked.connect(self.sekil_tahmin_et)
        self.m=True
        self.gb_temel_islemler.setGeometry(QtCore.QRect(150,50, 1450, 600))
        #template matching resim kesme olayları baslangic:
        self.gv_source.mousePressEvent=self.mousePressEvent
        self.gv_source.mouseMoveEvent=self.mouseMoveEvent
        self.gv_source.mouseReleaseEvent=self.mouseReleaseEvent
        #template matching resim kesme olayları son
        self.pb_erosion_upload_image.clicked.connect(self.erosion_upload_image)
        self.pb_erosion_dilation.clicked.connect(self.erosion_dilation)
        #----FaceDetection----
        self.pb_facedetection_upload_image.clicked.connect(self.on_pb_faced_upload)
        self.pb_face_detection.clicked.connect(self.on_pb_facedetection)
        self.pb_fd_yoklama.clicked.connect(self.on_pb_devamsizlik_al)
  
#---------Gorsel Showlar Baslangic ---------------------#  
    def main_menu_clicked(self):
        if self.gb_main_menu.height()==0:
            self.animation=QPropertyAnimation(self.gb_main_menu,"geometry")
            self.animation.setDuration(500)
            self.animation.setStartValue(QRect(0, 48, 150, 0))
            self.animation.setEndValue(QRect(0, 48, 150, 210))
            self.animation.start()
        else:
            self.animation=QPropertyAnimation(self.gb_main_menu,"geometry")
            self.animation.setDuration(500)
            self.animation.setStartValue(QRect(0, 48, 150,210))
            self.animation.setEndValue(QRect(0, 48, 150, 0))
            self.animation.start()
    
    #Main Menu Elemanlar
    def mm_temel_islemler(self):
        self.animasyon_baslat(self.gb_temel_islemler,150,50,1450,720)
        self.sifirla()
    
    def mm_mantiksal_islemler(self):
        self.animasyon_baslat(self.gb_mantiksal_islemler,150,50,1450,500)
        self.sifirla()
            
    def mm_etiketleme(self):
        self.animasyon_baslat(self.gb_labeling,150,50,1450,600)
        self.sifirla()
    
    def mm_gurultu_olusturma(self):
        self.animasyon_baslat(self.gb_gurultu_olustur,150,50,1450,600)
        self.sifirla()

    def mm_erosion(self):
        self.animasyon_baslat(self.gb_erosion,150, 50, 1450, 600)
        self.sifirla()
        
    def mm_template(self):
        self.animasyon_baslat(self.gb_template,150,50,1450,700)
        self.sifirla()
    
    def mm_face_detection(self):
        self.animasyon_baslat(self.gb_face_detection,150,50,1450,700)
        self.sifirla()
        self.verileri_tabloya_dok(self.verileri_cek(),self.tbl_devamsizlik)
            
    def animasyon_baslat(self,animasyon,x,y,w,h):
        if animasyon.width()==0:
            self.animation=QPropertyAnimation(animasyon,"geometry")
            self.animation.setDuration(1000)
            self.animation.setStartValue(QRect(x, y, 0, 0))
            self.animation.setEndValue(QRect(x, y, w, h))
            self.animation.start()
        else :
            self.animation=QPropertyAnimation(animasyon,"geometry")
            self.animation.setDuration(1000)
            self.animation.setStartValue(QRect(x, y, w, h))
            self.animation.setEndValue(QRect(x, y, 0, 0))
            self.animation.start()
            
            
    def sifirla(self):
        x=150
        y=50
        self.gb_temel_islemler.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_mantiksal_islemler.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_labeling.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_gurultu_olustur.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_erosion.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_template.setGeometry(QtCore.QRect(x, y, 0, 0))
        self.gb_face_detection.setGeometry(QtCore.QRect(x, y, 0, 0))

        
    def shutdown(self):
        sys.exit()
        
    #Tab1 deki menu butonunun click olayı
    def menu_clicked(self):
        if self.m:
            self.animation=QPropertyAnimation(self.gb_menu,"geometry")
            self.animation.setDuration(1000)
            self.animation.setStartValue(QRect(10, 70, 0, 0))
            self.animation.setEndValue(QRect(10, 70, 390, 530))
            self.animation.start()
            self.m=False
        else:
            self.animation=QPropertyAnimation(self.gb_menu,"geometry")
            self.animation.setDuration(1000)
            self.animation.setStartValue(QRect(10, 70, 390, 530))
            self.animation.setEndValue(QRect(10, 70, 0, 0))
            self.animation.start()
            self.m=True

#---------Gorsel Showlar Son ---------------------#  

    #Qgraphicsview da resim gostermek icin yazılan fonksiyon
    def show_image(self,img_name,width,height):
        pixMap=QtGui.QPixmap(img_name)
        pixMap=pixMap.scaled(width-5,height-5)
        pixItem=QtGui.QGraphicsPixmapItem(pixMap)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        return scene
    #Qgraphicsview da pil ile acilan resimleri gostermek icin yazılan fonksiyon
    def show_pil_image(self,img,width,height):
        show_image=ImageQt(img)
        pixMap=QtGui.QPixmap.fromImage(show_image)
        pixMap=pixMap.scaled(width-5,height-5)
        pixItem=QtGui.QGraphicsPixmapItem(pixMap)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        return scene
    
    #Gurultu olustur tabindaki slider nesnesinin valuechanged olayi    
    def slider_value_changed(self):
        deger=self.slider_gurultu.value()
        self.lbl_slider.setText(str(deger))


#--------------Temel İslemler Baslangic ------------------------------#

            
    #Tab1 deki slider , image rotate icin kullaniliyor
    def rotate_img(self):
        val=self.t1_hs_rotate.value()
        self.t1_hs_lbl.setText(str(val))
        img=Image.open(self.fileName)
        img=img.rotate(int(val)).save("./resource/rotate.png")
        self.w_r,self.h_r=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.show_image("./resource/rotate.png",self.w_r,self.h_r))
    
        
    def image2gray(self,image,width,height):
        resim=Image.open(image)
        w,h=resim.size
        grayimg=Image.new('RGB', (w,h), "black")
        pixMap=grayimg.load()
        for x in range(w):
            for y in range(h):
                r,g,b=resim.getpixel((x,y))[:3]
                gray=int(0.2989*r+0.5870*g+0.1140*b)
                pixMap[x,y]=(gray,gray,gray)
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(grayimg,width,height)
        return scene
    
    def image2binary(self,image,width,height):
        resim=Image.open(image)
        w,h=resim.size
        binaryimg=Image.new('RGB', (w,h), "black")
        pixelMap=binaryimg.load()
        for x in range(w):
            for y in range(h):
                r,g,b=resim.getpixel((x,y))[:3]
                gray=int(0.2989*r+0.5870*g+0.1140*b)
                if gray<128:
                    pixelMap[x,y]=(0,0,0)
                else:
                    pixelMap[x,y]=(255,255,255)
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(binaryimg,width,height)
        return scene
    
    def yeniden_boyutlandir(self,image,width,height,w,h):
        from skimage.transform import resize
        resim=io.imread(image)
        resize_image=resize(resim,(width,height))
        io.imsave("./resource/resize_image.jpg",resize_image)
        scene=QGraphicsScene()
        scene=self.show_image("./resource/resize_image.jpg",w,h)
        return scene
#--------------Temel İslemler Son ------------------------------#
#************************************************************************#
#------ Kenar Algilama Baslangic ----------------------------------- #    
    def sobel_filter(self,image,width,height):
        resim=Image.open(image)
        w,h=resim.size
        binaryimg=Image.new('RGB', (w,h), "black")
        pixelMap=binaryimg.load()
        for x in range(w):
            for y in range(h):
                r,g,b=resim.getpixel((x,y))[:3]
                gray=int(0.2989*r+0.5870*g+0.1140*b)
                if gray<128:
                    pixelMap[x,y]=(0,0,0)
                else:
                    pixelMap[x,y]=(255,255,255)
        im=binaryimg
        dx=ndimage.sobel(im,0)
        dy=ndimage.sobel(im,1)
        mag=np.hypot(dx,dy)
        mag*=255.0/np.max(mag)
        sobel_i=mag
        io.imsave("./resource/sobel.jpg",sobel_i)
        scene=QGraphicsScene()
        scene=self.show_image("./resource/sobel.jpg",width,height)
        return scene
    
    def canny_edges(self,image,width,height):
        img = cv2.imread(image,0)
        edges = cv2.Canny(img,100,200)
        cv2.imwrite("./resource/canny_edge.png",edges)
        scene=QGraphicsScene()
        scene=self.show_image("./resource/canny_edge.png",width,height)
        return scene
    
    def prewitt(self,img,width,height):
        from skimage.filter import prewitt
        from skimage.color import rgb2gray
        image=io.imread(img)
        gray_image=rgb2gray(image)
        pre_image=prewitt(gray_image)
        io.imsave("./resource/prewitt.png",pre_image)
        scene=QGraphicsScene()
        scene=self.show_image("./resource/prewitt.png",width,height)
        return scene
    
    def threshold(self,img_name,w,h):
        image = io.imread(img_name)
        width, height = image.shape[:2] 
        for x in range(width):
            for y in range(height):
                r,g,b=image[x,y][:3]
                gray=int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                if gray<128:
                    image[x,y]=(0,0,0)
                else:
                    image[x,y]=(255,255,255)
        io.imsave("./resource/threshold.png",image)
        scene=QGraphicsScene()
        scene=self.show_image("./resource/threshold.png",w,h)
        return scene
        
        
#------ Kenar Algilama Son ----------------------------------- #   
        
#------------------Mantiksal Islemler Baslangic----------------#
    def _not(self,img,width,height):
        image=Image.open(img)
        pixelMap=image.load()
        imageNew=Image.new(image.mode,image.size)
        pixelNew=imageNew.load()
        for i in range(0,image.size[0]):
            for j in range(0,image.size[1]):
                a,b,c=pixelMap[i,j]
                pixelNew[i,j]=255-a,255-b,255-c
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(imageNew,width,height)
        return scene
    
    def _or(self,imgA,imgB,width,height):
        imA=Image.open(imgA)
        imB=Image.open(imgB)
        pixelMapA=imA.load()
        pixelMapB=imB.load()
        imageNew=Image.new(imA.mode,imA.size)
        pixelNew=imageNew.load()
        
        for i in range(0,imA.size[0]):
            for j in range(0,imA.size[1]):
                a,b,c=pixelMapA[i,j]
                d,e,f=pixelMapB[i,j]
                pixelNew[i,j]=a or d, b or e , c or f
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(imageNew,width,height)
        return scene
    
    def _and(self,imgA,imgB,width,height):
        imA=Image.open(imgA)
        imB=Image.open(imgB)
        pixelMapA=imA.load()
        pixelMapB=imB.load()
        imageNew=Image.new(imA.mode,imA.size)
        pixelNew=imageNew.load()
        
        for i in range(0,imA.size[0]):
            for j in range(0,imA.size[1]):
                a,b,c=pixelMapA[i,j]
                d,e,f=pixelMapB[i,j]
                pixelNew[i,j]=a and d, b and e , c and f
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(imageNew,width,height)
        return scene
        
    def _andNot(self,imgA,imgB,width,height):
        image=Image.open(imgB)
        imA=Image.open(imgA)
        pixelMap=image.load()
        not_b=Image.new(image.mode,image.size)
        pixels=not_b.load()
        
        for i in range(0,image.size[0]):
            for j in range(0,image.size[1]):
                a,b,c=pixelMap[i,j]
                pixels[i,j]=255-a,255-b,255-c
        imB=not_b
        pixelMapA=imA.load()
        pixelMapB=imB.load()
        imageNew=Image.new(imA.mode,imA.size)
        pixelNew=imageNew.load()
        
        for i in range(0,imA.size[0]):
            for j in range(0,imA.size[1]):
                a,b,c=pixelMapA[i,j]
                d,e,f=pixelMapB[i,j]
                pixelNew[i,j]=a and d, b and e , c and f
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(imageNew,width,height)
        return scene
    
    def _xor(self,imgA,imgB,width,height):
        from operator import xor
        imA=Image.open(imgA)
        imB=Image.open(imgB)
        pixelMapA=imA.load()
        pixelMapB=imB.load()
        imageNew=Image.new(imA.mode,imA.size)
        pixelNew=imageNew.load()
        
        for i in range(0,imA.size[0]):
            for j in range(0,imA.size[1]):
                a,b,c=pixelMapA[i,j]
                d,e,f=pixelMapB[i,j]
                pixelNew[i,j]=xor(a,d), xor(b,e) , xor(c,f)
        
        scene=QGraphicsScene()
        scene=self.show_pil_image(imageNew,width,height)
        return scene

    def mantiksal_combobox(self,currentindex):
        self.w,self.h=self.t2_gv_sonuc.width(),self.t2_gv_sonuc.height()
        if currentindex==0:#not işlemi
            self.t2_gv_sonuc.setScene(self._not(self.fileName_a,self.w,self.h))
        elif currentindex==1:#and işlemi
            self.t2_gv_sonuc.setScene(self._and(self.fileName_a,self.fileName_b,self.w,self.h))
        elif currentindex==2:#or işlemi
            self.t2_gv_sonuc.setScene(self._or(self.fileName_a,self.fileName_b,self.w,self.h))
        elif currentindex==3:#and not işlemi
            self.t2_gv_sonuc.setScene(self._andNot(self.fileName_a,self.fileName_b,self.w,self.h))
        elif currentindex==4:#xor işlemi
            self.t2_gv_sonuc.setScene(self._xor(self.fileName_a,self.fileName_b,self.w,self.h))
#------------------Mantiksal Islemler Son----------------#   
#-----------------Labeling Baslangic--------------------
    
    def sekil_tahmin_et(self):
        self.t3_lbl_tahmin.setText(self.sekil_bilgisi(self.tahmin_resmi))
        
    def sekil_bilgisi(self,img_name):
        Data=[]
        work_dir="./resource/labeling"
        folderList=os.listdir(work_dir)
        for i,folder_name in enumerate(folderList):
            folder=os.listdir(work_dir+"/"+folder_name)
            test=[]
            for file_name in folder:
                s=self.ssim(work_dir+"/"+folder_name+"/"+file_name,img_name)
                test.append(s)
            m_m=max(test)
            Data.append((folder_name,m_m))    
        max_list=sorted(Data, key=lambda Data: Data[1])
        print max_list
        mm=max_list[len(max_list)-1][0]
        return mm
        
    def labeling(self,img,width,height):
        self.t3_cb_shapes.clear()
        image=color.rgb2gray(io.imread(img))
        cleared=clear_border(image)
        label_image=label(cleared)
        
        for i,region in enumerate(regionprops(label_image)):
            minr,minc,maxr,maxc=region.bbox
            fark=maxr-minr
            fark2=maxc-minc
            fark=200-fark
            fark2=200-fark2
            a=fark/2
            b=fark-a
            c=fark2/2
            d=fark2-c
            newminr=minr-a
            newmaxr=maxr+b
            newminc=minc-c
            newmaxc=maxc+d
            fark=newmaxr-newminr
            fark2=newmaxc-newminc
            fark=200-fark
            fark2=200-fark2
            newmaxr=newmaxr+fark
            newmaxc=newmaxc+fark2
            bolge=image[newminr:newmaxr,newminc:newmaxc]
            io.imsave("./resource/"+str(i)+'.png',bolge)
            self.t3_cb_shapes.addItem("Sekil "+str(i+1))
        
        scene=QGraphicsScene()
        scene=self.show_image("./resource/0.png",width,height)
        return scene
        
    def labeling_combobox(self,currentindex):
        self.w,self.h=self.t3_gv_sonuc.width(),self.t3_gv_sonuc.height()
        self.t3_gv_sonuc.setScene(self.show_image("./resource/"+str(currentindex)+".png",self.w,self.h))
        self.tahmin_resmi="./resource/"+str(currentindex)+".png"
      
    
#-----------------Labeling Son--------------------

#-----------Erosion & Dilation ------------------ Baslangic
    def erosion_upload_image(self):
        self.fileName_erosion=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        w,h=self.gv_erosion_source.width(),self.gv_erosion_source.height()
        self.gv_erosion_source.setScene(self.show_image(self.fileName_erosion,w,h))
    
    def erosion_dilation(self):
        it=self.le_erosion_iterasyon.text()
        w,h=self.gv_erosion_result.width(),self.gv_erosion_result.height()
        if self.fileName_erosion:
            img = cv2.imread(self.fileName_erosion,0)
            kernel = np.ones((5,5),np.uint8)
            if self.rb_erosion.isChecked():
                erosion = cv2.erode(img,kernel,iterations =int(it))
                io.imsave("./resource/erosion_dilation.png",erosion)
                self.gv_erosion_result.setScene(self.show_image("./resource/erosion_dilation.png",w,h))
            elif self.rb_dilation.isChecked():
                dilation = cv2.dilate(img,kernel,iterations = int(it))
                io.imsave("./resource/erosion_dilation.png",dilation)
                self.gv_erosion_result.setScene(self.show_image("./resource/erosion_dilation.png",w,h))
#-----------Erosion & Dilation ------------------ Son


#--------- Template Matching Baslangic ----------------#   
#template matching resim kesme işlemi -baslangic
    def mousePressEvent(self,eventQMouseEvent): #mouse sol click
        self.test=QPoint(190,155) #bu nokta QGraphicsViewın x,y noktası
        self.originQPoint = eventQMouseEvent.pos() #mouseın tıkladığı yeri aliyoruz
        self.originQPoint=self.originQPoint+self.test #x,y konumunu ekliyoruz
        self.currentQRubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)#Rubberband tanimlaniyor
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))#Rubberband cizdiriliyor
        self.currentQRubberBand.show()
        
    def mouseMoveEvent (self, eventQMouseEvent):
        new_pos=eventQMouseEvent.pos()+self.test #rubber band tam QGraphicsviewın üzerinde olsun diye konumlar ekleniyor
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint,new_pos ).normalized())#Rubberband cizdiriliyor

    def mouseReleaseEvent (self, eventQMouseEvent):
        x=self.currentQRubberBand.geometry().x()-190 #Kesme işlemi yapılırken eklenen konumlar siliniyor
        y=self.currentQRubberBand.geometry().y()-155
        w=self.currentQRubberBand.geometry().width()
        h=self.currentQRubberBand.geometry().height()
        self.currentQRubberBand.hide()#rubber band gizleniyor
        currentQRect = QRect(x,y,w,h)
        self.currentQRubberBand.deleteLater() #rubber band siliniyor
        cropQPixmap = self.pixMap_t.copy(currentQRect) # resim kesiliyor
        cropQPixmap.save('./resource/tm_crop_image.png')#kesilen resim kayıt ediliyor
        w,h=self.gv_parca.width(),self.gv_parca.height()
        self.gv_parca.setScene(self.show_image('./resource/tm_crop_image.png',w,h))#graphicsview da gösteriliyor
#template matching resim kesme işlemi -son
        
    def template_matching(self,sourceimage,parca):
        import cv2
        bimage=io.imread(sourceimage)

        img = cv2.imread(sourceimage,0)
        img2 = img.copy()
        template = cv2.imread(parca,0)
        w, h = template.shape[::-1]
        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        i=0
        for meth in methods:
            i=i+1
            img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img,top_left, bottom_right, 255, 4)
            bolge=bimage[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
            io.imsave("./resource/b"+str(i)+".png",bolge)
            io.imsave("./resource/mr"+str(i)+".png",res)
            io.imsave("./resource/cv"+str(i)+".png",img)

#--------- Template Matching Son ------ ----------------#   
    
    def salt_and_pepper_noise(self,img,yuzdelikdeger,w,h):
        from random import randint
        image=Image.open(img)
        width=image.size[0]
        height=image.size[1]
        pixelMap=image.load()
        oran=(width*height*yuzdelikdeger)/100
        
        for i in range(0,oran):
            rwidth=randint(0,width-1)
            rheight=randint(0,height-1)
            saltorpepper=randint(0,1)
            
            if saltorpepper==0:
                pixelMap[rwidth,rheight]=(0,0,0)
            else:
                pixelMap[rwidth,rheight]=(255,255,255)
        
        io.imsave("./resource/salt_pepper.png",image)
        scene=QGraphicsScene()
        scene=self.show_pil_image(image,w,h)
        return scene
    
    def equal_histogram(self,image,w,h):
        self.w_h,self.h_h=self.t1_gv_hist_once.width(),self.t1_gv_hist_once.height()
        img =cv2.imread(image,0)
        plt.hist(img.ravel(),256,[0,256]); plt.savefig("./resource/once.png")
        equ = cv2.equalizeHist(img)
        io.imsave("./resource/equalhistogram.png",equ)
        self.lbl_hist_mse.setText("MSE: "+str(round(self.mse(self.fileName,"./resource/equalhistogram.png"),2)))
        self.lbl_hist_ssim.setText("SSIM: "+str(round(self.ssim(self.fileName,"./resource/equalhistogram.png"),2)))
        plt.cla()
        plt.hist(equ.ravel(),256,[0,256]); plt.savefig("./resource/sonra.png")
        self.t1_gv_hist_once.setScene(self.show_image("./resource/once.png",self.w_h,self.h_h))
        self.t1_gv_hist_sonra.setScene(self.show_image("./resource/sonra.png",self.w_h,self.h_h))
        
        scene=QGraphicsScene()
        scene=self.show_image("./resource/equalhistogram.png",w,h)
        return scene


#---------------------Face Detection------- baslangic------------
    def on_pb_faced_upload(self):
        self.fileName=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        w,h=self.gv_facedetection_source.width(),self.gv_facedetection_source.height()
        self.gv_facedetection_source.setScene(self.show_image(self.fileName,w,h))
    
    def on_pb_facedetection(self):
        names=FaceDetection.predict(self.fileName)
        w,h=self.gv_facedetection_source.width(),self.gv_facedetection_source.height()
        self.gv_facedetection_source.setScene(self.show_image("./resource/face_detection.jpg",w,h))
        self.list_ogrenci.clear()
        for n in names:
            item=QListWidgetItem(n)
            self.list_ogrenci.addItem(item)
    
    def on_pb_devamsizlik_al(self):
        gun,ay,yil=self.dateEdit.date().day(),self.dateEdit.date().month(),self.dateEdit.date().year()
        s,d=self.timeEdit.time().hour(),self.timeEdit.time().minute()
        tarih=str(yil)+"."+str(ay)+"."+str(gun)
        saat=str(s)+":"+str(d)
        
        tum_ogrenciler=[]
        for i in range(self.list_tum_ogrenci.count()):
            tum_ogrenciler.append(str(self.list_tum_ogrenci.item(i).text()))
            
        gelen_ogrenciler=[]
        for i in range(self.list_ogrenci.count()):
            gelen_ogrenciler.append(str(self.list_ogrenci.item(i).text()))
            
        for i in tum_ogrenciler:
            if i in gelen_ogrenciler:
                query='INSERT INTO devamsizlik(tarih,saat,ogrenci_adi,devamsizlik_durumu) VALUES("%s","%s","%s","%s")'%(tarih,saat,i,"burada")
            else:
                query='INSERT INTO devamsizlik(tarih,saat,ogrenci_adi,devamsizlik_durumu) VALUES("%s","%s","%s","%s")'%(tarih,saat,i,"yok")
            
            self.cursor.execute(query)
        
        self.verileri_tabloya_dok(self.verileri_cek(),self.tbl_devamsizlik)

    def verileri_cek(self):
        query=("SELECT * FROM `devamsizlik`")
        bilgi=[]
        self.cursor.execute(query)
        data=self.cursor.fetchall()
        print data
        for a in data:
            bilgi.append(a)
        bilgi=np.array(bilgi)
        return bilgi
            
    def verileri_tabloya_dok(self,table_value,table_name):
        num_rows=len(table_value) #tablonun satir sayisi aliniyor
        num_column=len(table_value[0]) #tablonun sutun sayisi aliniyor
        table_name.clear()        #tabloda onceden deger var ise temizleniyor
        table_name.setColumnCount(num_column) #tablonun sutun sayisi set ediliyor
        table_name.setRowCount(num_rows) #tablonun satir sayisi set ediliyor
        for rowNumber,row in enumerate(table_value):#tabloya eklenecek deger satir satir ve
            for columnNumber in range(0,len(table_value[0])):#sutun sutun okunuyor
                table_name.setItem(rowNumber,columnNumber,QtGui.QTableWidgetItem(str(row[columnNumber]))) #okunan degerler tabloya set ediliyor
        
#---------------------Face Detection------- Son------------
    def mse(self,imgA, imgB):
        imageA=cv2.imread(imgA)
        imageB=cv2.imread(imgB)
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return round(err,2)
    
    def ssim(self,imgA,imgB):
        from skimage.measure import structural_similarity as ss
        imageA=cv2.imread(imgA)
        imageB=cv2.imread(imgB)
        imageA=cv2.cvtColor(imageA , cv2.COLOR_BGR2GRAY)
        imageB=cv2.cvtColor(imageB , cv2.COLOR_BGR2GRAY)
        s=ss(imageA,imageB)
        return round(s,2)
    
    def psnr(self,imgA, imgB):
        img1=cv2.imread(imgA)
        img2=cv2.imread(imgB)
        mse = np.mean( (img1 - img2) ** 2 )
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return round(20 * math.log10(PIXEL_MAX / math.sqrt(mse)),2)
#-----------------------BUTTON CLICK OLAYLARI BASLANGIC-----------------------#        
    @QtCore.pyqtSignature("bool")
    def on_pb_upload_img_clicked(self):
        self.fileName_t=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.w,self.h=self.gv_source.width(),self.gv_source.height()
        self.pixMap_t=QtGui.QPixmap(self.fileName_t)
        self.pixMap_t=self.pixMap_t.scaled(self.w-5,self.h-5)
        pixItem=QtGui.QGraphicsPixmapItem(self.pixMap_t)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        self.gv_source.setScene(scene)
        
    @QtCore.pyqtSignature("bool")
    def on_pb_template_matching_clicked(self):
        aranan='./resource/tm_crop_image.png'
        self.template_matching(self.fileName_t,aranan)
        self.w,self.h=self.gv_cv1.width(),self.gv_cv1.height()
        self.gv_cv1.setScene(self.show_image("./resource/cv1.png",self.w,self.h))
        self.gv_cv2.setScene(self.show_image("./resource/cv2.png",self.w,self.h))
        self.gv_cv3.setScene(self.show_image("./resource/cv3.png",self.w,self.h))
        self.gv_cv4.setScene(self.show_image("./resource/cv4.png",self.w,self.h))
        self.gv_cv5.setScene(self.show_image("./resource/cv5.png",self.w,self.h))
        self.gv_cv6.setScene(self.show_image("./resource/cv6.png",self.w,self.h))
        self.gv_mr1.setScene(self.show_image("./resource/mr1.png",self.w,self.h))
        self.gv_mr2.setScene(self.show_image("./resource/mr2.png",self.w,self.h))
        self.gv_mr3.setScene(self.show_image("./resource/mr3.png",self.w,self.h))
        self.gv_mr4.setScene(self.show_image("./resource/mr4.png",self.w,self.h))
        self.gv_mr5.setScene(self.show_image("./resource/mr5.png",self.w,self.h))
        self.gv_mr6.setScene(self.show_image("./resource/mr6.png",self.w,self.h))
        self.gv_r1.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_r2.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_r3.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_r4.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_r5.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_r6.setScene(self.show_image(aranan,self.w,self.h))
        self.gv_b1.setScene(self.show_image("./resource/b1.png",self.w,self.h))
        self.gv_b2.setScene(self.show_image("./resource/b2.png",self.w,self.h))
        self.gv_b3.setScene(self.show_image("./resource/b3.png",self.w,self.h))
        self.gv_b4.setScene(self.show_image("./resource/b4.png",self.w,self.h))
        self.gv_b5.setScene(self.show_image("./resource/b5.png",self.w,self.h))
        self.gv_b6.setScene(self.show_image("./resource/b6.png",self.w,self.h))
        self.lb_mse1.setText("MSE  : " +str(self.mse(aranan,"./resource/b1.png")))
        self.lb_mse2.setText("MSE  : " +str(self.mse(aranan,"./resource/b2.png")))
        self.lb_mse3.setText("MSE  : " +str(self.mse(aranan,"./resource/b3.png")))
        self.lb_mse4.setText("MSE  : " +str(self.mse(aranan,"./resource/b4.png")))
        self.lb_mse5.setText("MSE  : " +str(self.mse(aranan,"./resource/b5.png")))
        self.lb_mse6.setText("MSE  : " +str(self.mse(aranan,"./resource/b6.png")))
        self.lb_ssim1.setText("SSIM : "+str(self.ssim(aranan,"./resource/b1.png")))
        self.lb_ssim2.setText("SSIM : "+str(self.ssim(aranan,"./resource/b2.png")))
        self.lb_ssim3.setText("SSIM : "+str(self.ssim(aranan,"./resource/b3.png")))
        self.lb_ssim4.setText("SSIM : "+str(self.ssim(aranan,"./resource/b4.png")))
        self.lb_ssim5.setText("SSIM : "+str(self.ssim(aranan,"./resource/b5.png")))
        self.lb_ssim6.setText("SSIM : "+str(self.ssim(aranan,"./resource/b6.png")))
        self.lb_psnr1.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))
        self.lb_psnr2.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))
        self.lb_psnr3.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))
        self.lb_psnr4.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))
        self.lb_psnr5.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))
        self.lb_psnr6.setText("PSNR : "+str(self.psnr(aranan,"./resource/b6.png")))

            
        
    @QtCore.pyqtSignature("bool")
    def on_t1_resim_yukle_clicked(self):
        self.fileName=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.w,self.h=self.t1_gw_orijinal.width(),self.t1_gw_orijinal.height()
        self.t1_gw_orijinal.setScene(self.show_image(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_gray_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.image2gray(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_binary_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.image2binary(self.fileName,self.w,self.h))
        
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_resize_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.yeniden_boyutlandir(self.fileName,int(self.t1_te_width.toPlainText()),int(self.t1_te_height.toPlainText()),self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_sobel_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.sobel_filter(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_canny_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.canny_edges(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_prewitt_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.prewitt(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_threshold_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.threshold(self.fileName,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t2_pb_g_yukle_a_clicked(self):
        self.fileName_a=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.w,self.h=self.t2_gv_a.width(),self.t2_gv_a.height()
        self.t2_gv_a.setScene(self.show_image(self.fileName_a,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_t2_pb_g_yukle_b_clicked(self):
        self.fileName_b=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.w,self.h=self.t2_gv_b.width(),self.t2_gv_b.height()
        self.t2_gv_b.setScene(self.show_image(self.fileName_b,self.w,self.h))
    @QtCore.pyqtSignature("bool")
    def on_t3_pb_upload_image_clicked(self):
        self.fileName_t3=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.w,self.h=self.t3_gv_source.width(),self.t3_gv_source.height()
        self.t3_gv_source.setScene(self.show_image(self.fileName_t3,self.w,self.h))
        
    @QtCore.pyqtSignature("bool")
    def on_t3_pb_labeling_clicked(self):
        self.w,self.h=self.t3_gv_sonuc.width(),self.t3_gv_sonuc.height()
        self.t3_gv_sonuc.setScene(self.labeling(self.fileName_t3,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_pb_gurultu_upload_image_clicked(self):
        self.w,self.h=self.gv_gurultu_olusturma.width(),self.gv_gurultu_olusturma.height()
        self.fileName_gurultu=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Düzenlenecek dosyayı seçin",".",u"resim dosyalari(*.jpg *.png *.gif)"))
        self.gv_gurultu_olusturma.setScene(self.show_image(self.fileName_gurultu,self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_pb_gurultu_olustur_clicked(self):
        self.w,self.h=self.gv_gurultu_sonuc.width(),self.gv_gurultu_sonuc.height()
        self.gv_gurultu_sonuc.setScene(self.salt_and_pepper_noise(self.fileName_gurultu,self.slider_gurultu.value(),self.w,self.h))
        self.lbl_gurultu_mse.setText("MSE: "+str(round(self.mse(self.fileName_gurultu,"./resource/salt_pepper.png"),2)))
        self.lbl_gurultu_ssim.setText("SSIM: "+str(round(self.ssim(self.fileName_gurultu,"./resource/salt_pepper.png"),2)))
        self.lbl_gurultu_psnr.setText("PSNR: "+str(round(self.psnr(self.fileName_gurultu,"./resource/salt_pepper.png"),2)))
    
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_histogram_clicked(self):
        self.w,self.h=self.t1_gw_islem.width(),self.t1_gw_islem.height()
        self.t1_gw_islem.setScene(self.equal_histogram(self.fileName,self.w,self.h))
        
#-----------------------BUTTON CLICK OLAYLARI SON-----------------------------#            