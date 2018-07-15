# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:13:36 2018

@author: Bedirhan
"""

import numpy as np
from skimage import io
import cv2
import os
from sklearn.externals import joblib

METHOD = 'uniform'
P = 16
R = 2

def kullback_leibler_divergence(p, q):
    p = np.asarray(p)
    q = np.asarray(q)
    filt = np.logical_and(p != 0, q != 0)
    return np.sum(p[filt] * np.log2(p[filt] / q[filt]))

def match(refs, img):
    best_score = 10
    best_name = None
    lbp = img
    hist, _ = np.histogram(lbp, normed=True, bins=P + 2, range=(0, P + 2))
    for name, ref in refs.items():
        ref_hist, _ = np.histogram(ref, normed=True, bins=P + 2,
                                   range=(0, P + 2))
        score = kullback_leibler_divergence(hist, ref_hist)
        if score < best_score:
            best_score = score
            best_name = name

    return best_name[:len(best_name)-1]
    
def predict(image):
    refs=joblib.load("./facedata.pkl")
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    names=[]
    faces = face_cascade.detectMultiScale(gray, 2, 5)
    i=0
    for (x,y,w,h) in faces:
        i=i+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]
        sonuc=match(refs,roi_color)
        names.append(sonuc)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,sonuc,(x+10,y+h+30), font, 1,(255,0,0),2,cv2.LINE_AA)
        
    io.imsave("./resource/face_detection.jpg",img)
    return names

def save_model():
    refs={}
    work_dir="./FaceData"
    folderList=os.listdir(work_dir)
    for folder_name in folderList:
        folder=os.listdir(work_dir+"/"+folder_name)
        for i,file_name in enumerate(folder):
            val=io.imread(work_dir+"/"+folder_name+"/"+file_name)
            dictionary={folder_name+str(i):val}
            refs.update(dictionary)
            
    joblib.dump(refs,"./facedata.pkl")

