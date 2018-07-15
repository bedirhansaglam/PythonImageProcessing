# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created: Wed Jan 10 23:06:31 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1600, 700)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(1920, 1079))
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"background-color:white;}\n"
"QGraphicsView{\n"
"border:2px solid #31AF91}\n"
"QLabel{\n"
"color:#31AF91}\n"
"QComboBox {\n"
"    border: 1px solid #31AF91;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: #31AF91;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"color:#fff;\n"
"background-color:#31AF91;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"background-color:#31AF91;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #31AF91;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}"))
        self.gb_main_menu = QtGui.QGroupBox(Dialog)
        self.gb_main_menu.setGeometry(QtCore.QRect(0, 48, 150, 211))
        self.gb_main_menu.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"text-align: left;\n"
"padding-left:15px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #247CB5;\n"
"color: #fff;\n"
"}\n"
"#gb_main_menu{\n"
"background-color:#31AF91;}\n"
""))
        self.gb_main_menu.setTitle(_fromUtf8(""))
        self.gb_main_menu.setObjectName(_fromUtf8("gb_main_menu"))
        self.pb_menu_1 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_1.setGeometry(QtCore.QRect(0, 0, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_1.setFont(font)
        self.pb_menu_1.setStyleSheet(_fromUtf8(""))
        self.pb_menu_1.setObjectName(_fromUtf8("pb_menu_1"))
        self.pb_menu_2 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_2.setGeometry(QtCore.QRect(0, 30, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_2.setFont(font)
        self.pb_menu_2.setObjectName(_fromUtf8("pb_menu_2"))
        self.pb_menu_3 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_3.setGeometry(QtCore.QRect(0, 60, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_3.setFont(font)
        self.pb_menu_3.setObjectName(_fromUtf8("pb_menu_3"))
        self.pb_menu_4 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_4.setGeometry(QtCore.QRect(0, 90, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_4.setFont(font)
        self.pb_menu_4.setObjectName(_fromUtf8("pb_menu_4"))
        self.pb_menu_5 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_5.setGeometry(QtCore.QRect(0, 120, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_5.setFont(font)
        self.pb_menu_5.setObjectName(_fromUtf8("pb_menu_5"))
        self.pb_menu_6 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_6.setGeometry(QtCore.QRect(0, 150, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_6.setFont(font)
        self.pb_menu_6.setObjectName(_fromUtf8("pb_menu_6"))
        self.pb_menu_7 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_menu_7.setGeometry(QtCore.QRect(0, 180, 148, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Buxton Sketch"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_menu_7.setFont(font)
        self.pb_menu_7.setObjectName(_fromUtf8("pb_menu_7"))
        self.gb_temel_islemler = QtGui.QGroupBox(Dialog)
        self.gb_temel_islemler.setGeometry(QtCore.QRect(150, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_temel_islemler.setFont(font)
        self.gb_temel_islemler.setStyleSheet(_fromUtf8("#gb_temel_islemler{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_temel_islemler::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
"QGraphicsView{\n"
"border:2px solid #31AF91}"))
        self.gb_temel_islemler.setObjectName(_fromUtf8("gb_temel_islemler"))
        self.label = QtGui.QLabel(self.gb_temel_islemler)
        self.label.setGeometry(QtCore.QRect(420, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.t1_resim_yukle = QtGui.QPushButton(self.gb_temel_islemler)
        self.t1_resim_yukle.setGeometry(QtCore.QRect(60, 20, 48, 48))
        self.t1_resim_yukle.setStyleSheet(_fromUtf8("#t1_resim_yukle{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#t1_resim_yukle:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.t1_resim_yukle.setText(_fromUtf8(""))
        self.t1_resim_yukle.setObjectName(_fromUtf8("t1_resim_yukle"))
        self.gb_menu = QtGui.QGroupBox(self.gb_temel_islemler)
        self.gb_menu.setGeometry(QtCore.QRect(0, 70, 391, 531))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gb_menu.setFont(font)
        self.gb_menu.setTitle(_fromUtf8(""))
        self.gb_menu.setObjectName(_fromUtf8("gb_menu"))
        self.tabWidget_3 = QtGui.QTabWidget(self.gb_menu)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 10, 371, 511))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setStyleSheet(_fromUtf8("#tabWidget_3::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;}\n"
"#tabWidget_3::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"#tabWidget_3::tab {\n"
"    background: #31AF91;\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"color:#fff;\n"
"}\n"
"#tabWidget_3::tab:selected, QTabBar::tab:hover {\n"
"    background:#44F2C9;\n"
"}"))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 191, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(_fromUtf8("#groupBox_3{\n"
"color:#31AF91}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.t1_pb_resize = QtGui.QPushButton(self.groupBox_3)
        self.t1_pb_resize.setGeometry(QtCore.QRect(100, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_resize.setFont(font)
        self.t1_pb_resize.setStyleSheet(_fromUtf8("#t1_pb_resize{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_resize:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_resize.setObjectName(_fromUtf8("t1_pb_resize"))
        self.t1_te_height = QtGui.QTextEdit(self.groupBox_3)
        self.t1_te_height.setGeometry(QtCore.QRect(90, 80, 91, 31))
        self.t1_te_height.setObjectName(_fromUtf8("t1_te_height"))
        self.t1_te_width = QtGui.QTextEdit(self.groupBox_3)
        self.t1_te_width.setGeometry(QtCore.QRect(90, 40, 91, 31))
        self.t1_te_width.setObjectName(_fromUtf8("t1_te_width"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("#label_3{\n"
"color :#31AF91}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("#label_4{\n"
"color :#31AF91}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 20, 131, 171))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("#groupBox_2{\n"
"color:#31AF91}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.t1_hs_rotate = QtGui.QSlider(self.groupBox_2)
        self.t1_hs_rotate.setGeometry(QtCore.QRect(50, 40, 31, 121))
        self.t1_hs_rotate.setStyleSheet(_fromUtf8("#t1_hs_rotate:groove:vertical {\n"
"    background: #44F2C9;\n"
"    position: absolute;\n"
"    left: 4px; right: 4px;\n"
"}\n"
"#t1_hs_rotate:handle:vertical {\n"
"    height: 10px;\n"
"    background: #31AF91 ;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}"))
        self.t1_hs_rotate.setMaximum(360)
        self.t1_hs_rotate.setSingleStep(5)
        self.t1_hs_rotate.setOrientation(QtCore.Qt.Vertical)
        self.t1_hs_rotate.setObjectName(_fromUtf8("t1_hs_rotate"))
        self.t1_hs_lbl = QtGui.QLabel(self.groupBox_2)
        self.t1_hs_lbl.setGeometry(QtCore.QRect(60, 20, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t1_hs_lbl.setFont(font)
        self.t1_hs_lbl.setStyleSheet(_fromUtf8("#t1_hs_lbl{\n"
"color :#31AF91}"))
        self.t1_hs_lbl.setObjectName(_fromUtf8("t1_hs_lbl"))
        self.t1_pb_binary = QtGui.QPushButton(self.tab_8)
        self.t1_pb_binary.setGeometry(QtCore.QRect(230, 260, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_binary.setFont(font)
        self.t1_pb_binary.setStyleSheet(_fromUtf8("#t1_pb_binary{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_binary:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_binary.setObjectName(_fromUtf8("t1_pb_binary"))
        self.t1_pb_gray = QtGui.QPushButton(self.tab_8)
        self.t1_pb_gray.setGeometry(QtCore.QRect(50, 260, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_gray.setFont(font)
        self.t1_pb_gray.setStyleSheet(_fromUtf8("#t1_pb_gray{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_gray:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_gray.setObjectName(_fromUtf8("t1_pb_gray"))
        self.tabWidget_3.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.t1_pb_sobel = QtGui.QPushButton(self.tab_9)
        self.t1_pb_sobel.setGeometry(QtCore.QRect(10, 50, 175, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_sobel.setFont(font)
        self.t1_pb_sobel.setStyleSheet(_fromUtf8("#t1_pb_sobel{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_sobel:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_sobel.setObjectName(_fromUtf8("t1_pb_sobel"))
        self.t1_pb_canny = QtGui.QPushButton(self.tab_9)
        self.t1_pb_canny.setGeometry(QtCore.QRect(190, 50, 175, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_canny.setFont(font)
        self.t1_pb_canny.setStyleSheet(_fromUtf8("#t1_pb_canny{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_canny:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_canny.setObjectName(_fromUtf8("t1_pb_canny"))
        self.t1_pb_prewitt = QtGui.QPushButton(self.tab_9)
        self.t1_pb_prewitt.setGeometry(QtCore.QRect(10, 270, 175, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_prewitt.setFont(font)
        self.t1_pb_prewitt.setStyleSheet(_fromUtf8("#t1_pb_prewitt{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_prewitt:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_prewitt.setObjectName(_fromUtf8("t1_pb_prewitt"))
        self.t1_pb_threshold = QtGui.QPushButton(self.tab_9)
        self.t1_pb_threshold.setGeometry(QtCore.QRect(190, 270, 175, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_threshold.setFont(font)
        self.t1_pb_threshold.setStyleSheet(_fromUtf8("#t1_pb_threshold{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_threshold:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_threshold.setObjectName(_fromUtf8("t1_pb_threshold"))
        self.tabWidget_3.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.t1_pb_histogram = QtGui.QPushButton(self.tab_10)
        self.t1_pb_histogram.setGeometry(QtCore.QRect(10, 10, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t1_pb_histogram.setFont(font)
        self.t1_pb_histogram.setStyleSheet(_fromUtf8("#t1_pb_histogram{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t1_pb_histogram:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t1_pb_histogram.setObjectName(_fromUtf8("t1_pb_histogram"))
        self.groupBox = QtGui.QGroupBox(self.tab_10)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 351, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.t1_gv_hist_once = QtGui.QGraphicsView(self.groupBox)
        self.t1_gv_hist_once.setGeometry(QtCore.QRect(80, 80, 211, 151))
        self.t1_gv_hist_once.setObjectName(_fromUtf8("t1_gv_hist_once"))
        self.t1_gv_hist_sonra = QtGui.QGraphicsView(self.groupBox)
        self.t1_gv_hist_sonra.setGeometry(QtCore.QRect(80, 240, 211, 151))
        self.t1_gv_hist_sonra.setObjectName(_fromUtf8("t1_gv_hist_sonra"))
        self.lbl_hist_ssim = QtGui.QLabel(self.groupBox)
        self.lbl_hist_ssim.setGeometry(QtCore.QRect(170, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hist_ssim.setFont(font)
        self.lbl_hist_ssim.setStyleSheet(_fromUtf8("#lbl_hist_ssim{\n"
"color :#31AF91}"))
        self.lbl_hist_ssim.setObjectName(_fromUtf8("lbl_hist_ssim"))
        self.label_45 = QtGui.QLabel(self.groupBox)
        self.label_45.setGeometry(QtCore.QRect(10, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(_fromUtf8("#label_45{\n"
"color :#31AF91}"))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.lbl_hist_mse = QtGui.QLabel(self.groupBox)
        self.lbl_hist_mse.setGeometry(QtCore.QRect(10, 40, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hist_mse.setFont(font)
        self.lbl_hist_mse.setStyleSheet(_fromUtf8("#lbl_hist_mse{\n"
"color :#31AF91}"))
        self.lbl_hist_mse.setObjectName(_fromUtf8("lbl_hist_mse"))
        self.label_46 = QtGui.QLabel(self.groupBox)
        self.label_46.setGeometry(QtCore.QRect(10, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(_fromUtf8("#label_46{\n"
"color :#31AF91}"))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.label_47 = QtGui.QLabel(self.groupBox)
        self.label_47.setGeometry(QtCore.QRect(10, 240, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(_fromUtf8("#label_47{\n"
"color :#31AF91}"))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.tabWidget_3.addTab(self.tab_10, _fromUtf8(""))
        self.t1_gw_islem = QtGui.QGraphicsView(self.gb_temel_islemler)
        self.t1_gw_islem.setGeometry(QtCore.QRect(890, 80, 450, 450))
        self.t1_gw_islem.setStyleSheet(_fromUtf8(""))
        self.t1_gw_islem.setObjectName(_fromUtf8("t1_gw_islem"))
        self.label_2 = QtGui.QLabel(self.gb_temel_islemler)
        self.label_2.setGeometry(QtCore.QRect(900, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.t1_gw_orijinal = QtGui.QGraphicsView(self.gb_temel_islemler)
        self.t1_gw_orijinal.setGeometry(QtCore.QRect(410, 80, 450, 450))
        self.t1_gw_orijinal.setStyleSheet(_fromUtf8(""))
        self.t1_gw_orijinal.setObjectName(_fromUtf8("t1_gw_orijinal"))
        self.t1_pb_menu = QtGui.QPushButton(self.gb_temel_islemler)
        self.t1_pb_menu.setGeometry(QtCore.QRect(5, 20, 48, 48))
        self.t1_pb_menu.setStyleSheet(_fromUtf8("#t1_pb_menu{\n"
"color: grey;\n"
"            border-image: url(./icons/menu.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#t1_pb_menu:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/menu_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.t1_pb_menu.setText(_fromUtf8(""))
        self.t1_pb_menu.setObjectName(_fromUtf8("t1_pb_menu"))
        self.gb_top_menu = QtGui.QGroupBox(Dialog)
        self.gb_top_menu.setGeometry(QtCore.QRect(0, 0, 1920, 50))
        self.gb_top_menu.setStyleSheet(_fromUtf8("#gb_top_menu{\n"
"background-color:#31AF91;\n"
"border:2px solid #31AF91; }"))
        self.gb_top_menu.setTitle(_fromUtf8(""))
        self.gb_top_menu.setObjectName(_fromUtf8("gb_top_menu"))
        self.pb_exit = QtGui.QPushButton(self.gb_top_menu)
        self.pb_exit.setGeometry(QtCore.QRect(50, 0, 48, 48))
        self.pb_exit.setStyleSheet(_fromUtf8("#pb_exit{\n"
"color: grey;\n"
"            border-image: url(./icons/exit.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_exit:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/exit_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_exit.setText(_fromUtf8(""))
        self.pb_exit.setObjectName(_fromUtf8("pb_exit"))
        self.pb_main_menu = QtGui.QPushButton(self.gb_top_menu)
        self.pb_main_menu.setGeometry(QtCore.QRect(0, 0, 48, 48))
        self.pb_main_menu.setStyleSheet(_fromUtf8("#pb_main_menu{\n"
"color: grey;\n"
"            border-image: url(./icons/menu.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_main_menu:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/menu_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_main_menu.setText(_fromUtf8(""))
        self.pb_main_menu.setObjectName(_fromUtf8("pb_main_menu"))
        self.gb_mantiksal_islemler = QtGui.QGroupBox(Dialog)
        self.gb_mantiksal_islemler.setGeometry(QtCore.QRect(150, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_mantiksal_islemler.setFont(font)
        self.gb_mantiksal_islemler.setStyleSheet(_fromUtf8("#gb_mantiksal_islemler{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_mantiksal_islemler::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
""))
        self.gb_mantiksal_islemler.setObjectName(_fromUtf8("gb_mantiksal_islemler"))
        self.label_8 = QtGui.QLabel(self.gb_mantiksal_islemler)
        self.label_8.setGeometry(QtCore.QRect(840, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.t2_cb_mantiksal = QtGui.QComboBox(self.gb_mantiksal_islemler)
        self.t2_cb_mantiksal.setGeometry(QtCore.QRect(840, 250, 101, 22))
        self.t2_cb_mantiksal.setObjectName(_fromUtf8("t2_cb_mantiksal"))
        self.t2_cb_mantiksal.addItem(_fromUtf8(""))
        self.t2_cb_mantiksal.addItem(_fromUtf8(""))
        self.t2_cb_mantiksal.addItem(_fromUtf8(""))
        self.t2_cb_mantiksal.addItem(_fromUtf8(""))
        self.t2_cb_mantiksal.addItem(_fromUtf8(""))
        self.t2_gv_sonuc = QtGui.QGraphicsView(self.gb_mantiksal_islemler)
        self.t2_gv_sonuc.setGeometry(QtCore.QRect(960, 80, 400, 400))
        self.t2_gv_sonuc.setObjectName(_fromUtf8("t2_gv_sonuc"))
        self.t2_gv_a = QtGui.QGraphicsView(self.gb_mantiksal_islemler)
        self.t2_gv_a.setGeometry(QtCore.QRect(10, 80, 400, 400))
        self.t2_gv_a.setObjectName(_fromUtf8("t2_gv_a"))
        self.t2_gv_b = QtGui.QGraphicsView(self.gb_mantiksal_islemler)
        self.t2_gv_b.setGeometry(QtCore.QRect(430, 80, 400, 400))
        self.t2_gv_b.setObjectName(_fromUtf8("t2_gv_b"))
        self.t2_pb_g_yukle_a = QtGui.QPushButton(self.gb_mantiksal_islemler)
        self.t2_pb_g_yukle_a.setGeometry(QtCore.QRect(140, 20, 48, 48))
        self.t2_pb_g_yukle_a.setStyleSheet(_fromUtf8("#t2_pb_g_yukle_a{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#t2_pb_g_yukle_a:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.t2_pb_g_yukle_a.setText(_fromUtf8(""))
        self.t2_pb_g_yukle_a.setObjectName(_fromUtf8("t2_pb_g_yukle_a"))
        self.label_7 = QtGui.QLabel(self.gb_mantiksal_islemler)
        self.label_7.setGeometry(QtCore.QRect(960, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.t2_pb_g_yukle_b = QtGui.QPushButton(self.gb_mantiksal_islemler)
        self.t2_pb_g_yukle_b.setGeometry(QtCore.QRect(550, 20, 48, 48))
        self.t2_pb_g_yukle_b.setStyleSheet(_fromUtf8("#t2_pb_g_yukle_b{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#t2_pb_g_yukle_b:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.t2_pb_g_yukle_b.setText(_fromUtf8(""))
        self.t2_pb_g_yukle_b.setObjectName(_fromUtf8("t2_pb_g_yukle_b"))
        self.label_5 = QtGui.QLabel(self.gb_mantiksal_islemler)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.gb_mantiksal_islemler)
        self.label_6.setGeometry(QtCore.QRect(420, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gb_labeling = QtGui.QGroupBox(Dialog)
        self.gb_labeling.setGeometry(QtCore.QRect(250, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_labeling.setFont(font)
        self.gb_labeling.setStyleSheet(_fromUtf8("#gb_labeling{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_labeling::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
""))
        self.gb_labeling.setObjectName(_fromUtf8("gb_labeling"))
        self.t3_gv_sonuc = QtGui.QGraphicsView(self.gb_labeling)
        self.t3_gv_sonuc.setGeometry(QtCore.QRect(750, 120, 200, 200))
        self.t3_gv_sonuc.setObjectName(_fromUtf8("t3_gv_sonuc"))
        self.label_9 = QtGui.QLabel(self.gb_labeling)
        self.label_9.setGeometry(QtCore.QRect(750, 50, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.t3_cb_shapes = QtGui.QComboBox(self.gb_labeling)
        self.t3_cb_shapes.setGeometry(QtCore.QRect(750, 80, 201, 22))
        self.t3_cb_shapes.setObjectName(_fromUtf8("t3_cb_shapes"))
        self.t3_gv_source = QtGui.QGraphicsView(self.gb_labeling)
        self.t3_gv_source.setGeometry(QtCore.QRect(10, 70, 500, 500))
        self.t3_gv_source.setObjectName(_fromUtf8("t3_gv_source"))
        self.t3_pb_labeling = QtGui.QPushButton(self.gb_labeling)
        self.t3_pb_labeling.setGeometry(QtCore.QRect(530, 160, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.t3_pb_labeling.setFont(font)
        self.t3_pb_labeling.setStyleSheet(_fromUtf8("#t3_pb_labeling{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t3_pb_labeling:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t3_pb_labeling.setObjectName(_fromUtf8("t3_pb_labeling"))
        self.t3_pb_upload_image = QtGui.QPushButton(self.gb_labeling)
        self.t3_pb_upload_image.setGeometry(QtCore.QRect(10, 20, 48, 48))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t3_pb_upload_image.setFont(font)
        self.t3_pb_upload_image.setStyleSheet(_fromUtf8("#t3_pb_upload_image{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#t3_pb_upload_image:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/click.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.t3_pb_upload_image.setText(_fromUtf8(""))
        self.t3_pb_upload_image.setObjectName(_fromUtf8("t3_pb_upload_image"))
        self.t3_pb_tahmin = QtGui.QPushButton(self.gb_labeling)
        self.t3_pb_tahmin.setGeometry(QtCore.QRect(750, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t3_pb_tahmin.setFont(font)
        self.t3_pb_tahmin.setStyleSheet(_fromUtf8("#t3_pb_tahmin{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#t3_pb_tahmin:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.t3_pb_tahmin.setObjectName(_fromUtf8("t3_pb_tahmin"))
        self.t3_lbl_tahmin = QtGui.QLabel(self.gb_labeling)
        self.t3_lbl_tahmin.setGeometry(QtCore.QRect(760, 370, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.t3_lbl_tahmin.setFont(font)
        self.t3_lbl_tahmin.setText(_fromUtf8(""))
        self.t3_lbl_tahmin.setObjectName(_fromUtf8("t3_lbl_tahmin"))
        self.gb_gurultu_olustur = QtGui.QGroupBox(Dialog)
        self.gb_gurultu_olustur.setGeometry(QtCore.QRect(150, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_gurultu_olustur.setFont(font)
        self.gb_gurultu_olustur.setStyleSheet(_fromUtf8("#gb_gurultu_olustur{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_gurultu_olustur::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
""))
        self.gb_gurultu_olustur.setObjectName(_fromUtf8("gb_gurultu_olustur"))
        self.gv_gurultu_sonuc = QtGui.QGraphicsView(self.gb_gurultu_olustur)
        self.gv_gurultu_sonuc.setGeometry(QtCore.QRect(790, 80, 481, 481))
        self.gv_gurultu_sonuc.setObjectName(_fromUtf8("gv_gurultu_sonuc"))
        self.label_44 = QtGui.QLabel(self.gb_gurultu_olustur)
        self.label_44.setGeometry(QtCore.QRect(540, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.pb_gurultu_upload_image = QtGui.QPushButton(self.gb_gurultu_olustur)
        self.pb_gurultu_upload_image.setGeometry(QtCore.QRect(30, 30, 48, 48))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_gurultu_upload_image.setFont(font)
        self.pb_gurultu_upload_image.setStyleSheet(_fromUtf8("#pb_gurultu_upload_image{color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_gurultu_upload_image:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/click.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_gurultu_upload_image.setText(_fromUtf8(""))
        self.pb_gurultu_upload_image.setObjectName(_fromUtf8("pb_gurultu_upload_image"))
        self.lbl_slider = QtGui.QLabel(self.gb_gurultu_olustur)
        self.lbl_slider.setGeometry(QtCore.QRect(690, 134, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_slider.setFont(font)
        self.lbl_slider.setObjectName(_fromUtf8("lbl_slider"))
        self.pb_gurultu_olustur = QtGui.QPushButton(self.gb_gurultu_olustur)
        self.pb_gurultu_olustur.setGeometry(QtCore.QRect(540, 260, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_gurultu_olustur.setFont(font)
        self.pb_gurultu_olustur.setStyleSheet(_fromUtf8("#pb_gurultu_olustur{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#pb_gurultu_olustur:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.pb_gurultu_olustur.setObjectName(_fromUtf8("pb_gurultu_olustur"))
        self.gv_gurultu_olusturma = QtGui.QGraphicsView(self.gb_gurultu_olustur)
        self.gv_gurultu_olusturma.setGeometry(QtCore.QRect(30, 80, 481, 481))
        self.gv_gurultu_olusturma.setObjectName(_fromUtf8("gv_gurultu_olusturma"))
        self.slider_gurultu = QtGui.QSlider(self.gb_gurultu_olustur)
        self.slider_gurultu.setGeometry(QtCore.QRect(540, 200, 201, 21))
        self.slider_gurultu.setStyleSheet(_fromUtf8("#slider_gurultu:groove:horizontall {\n"
"    background: #44F2C9;\n"
"    position: absolute;\n"
"    left: 3px; right: 3px;\n"
"}\n"
"#slider_gurultu:handle:horizontall {\n"
"    height: 10px;\n"
"    background: #31AF91 ;\n"
"    margin: 0 4px; /* expand outside the groove */\n"
"}"))
        self.slider_gurultu.setMaximum(100)
        self.slider_gurultu.setSingleStep(10)
        self.slider_gurultu.setProperty("value", 0)
        self.slider_gurultu.setOrientation(QtCore.Qt.Horizontal)
        self.slider_gurultu.setObjectName(_fromUtf8("slider_gurultu"))
        self.lbl_gurultu_ssim = QtGui.QLabel(self.gb_gurultu_olustur)
        self.lbl_gurultu_ssim.setGeometry(QtCore.QRect(570, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gurultu_ssim.setFont(font)
        self.lbl_gurultu_ssim.setText(_fromUtf8(""))
        self.lbl_gurultu_ssim.setObjectName(_fromUtf8("lbl_gurultu_ssim"))
        self.lbl_gurultu_mse = QtGui.QLabel(self.gb_gurultu_olustur)
        self.lbl_gurultu_mse.setGeometry(QtCore.QRect(570, 420, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gurultu_mse.setFont(font)
        self.lbl_gurultu_mse.setText(_fromUtf8(""))
        self.lbl_gurultu_mse.setObjectName(_fromUtf8("lbl_gurultu_mse"))
        self.lbl_gurultu_psnr = QtGui.QLabel(self.gb_gurultu_olustur)
        self.lbl_gurultu_psnr.setGeometry(QtCore.QRect(570, 480, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gurultu_psnr.setFont(font)
        self.lbl_gurultu_psnr.setText(_fromUtf8(""))
        self.lbl_gurultu_psnr.setObjectName(_fromUtf8("lbl_gurultu_psnr"))
        self.gb_erosion = QtGui.QGroupBox(Dialog)
        self.gb_erosion.setGeometry(QtCore.QRect(150, 50, 0, 0))
        self.gb_erosion.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_erosion.setFont(font)
        self.gb_erosion.setStyleSheet(_fromUtf8("#gb_erosion{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_erosion::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
""))
        self.gb_erosion.setObjectName(_fromUtf8("gb_erosion"))
        self.gv_erosion_source = QtGui.QGraphicsView(self.gb_erosion)
        self.gv_erosion_source.setGeometry(QtCore.QRect(50, 110, 350, 350))
        self.gv_erosion_source.setObjectName(_fromUtf8("gv_erosion_source"))
        self.pb_erosion_upload_image = QtGui.QPushButton(self.gb_erosion)
        self.pb_erosion_upload_image.setGeometry(QtCore.QRect(350, 60, 48, 48))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_erosion_upload_image.setFont(font)
        self.pb_erosion_upload_image.setStyleSheet(_fromUtf8("#pb_erosion_upload_image{color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_erosion_upload_image:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_erosion_upload_image.setText(_fromUtf8(""))
        self.pb_erosion_upload_image.setObjectName(_fromUtf8("pb_erosion_upload_image"))
        self.gb_erosion_gb = QtGui.QGroupBox(self.gb_erosion)
        self.gb_erosion_gb.setGeometry(QtCore.QRect(490, 180, 231, 201))
        self.gb_erosion_gb.setStyleSheet(_fromUtf8("#gb_erosion_gb{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_erosion_gb::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
"QRadioButton{\n"
"color:#31AF91;}"))
        self.gb_erosion_gb.setTitle(_fromUtf8(""))
        self.gb_erosion_gb.setObjectName(_fromUtf8("gb_erosion_gb"))
        self.le_erosion_iterasyon = QtGui.QLineEdit(self.gb_erosion_gb)
        self.le_erosion_iterasyon.setGeometry(QtCore.QRect(160, 30, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_erosion_iterasyon.setFont(font)
        self.le_erosion_iterasyon.setStyleSheet(_fromUtf8("QLineEdit{\n"
"color:#31AF91;\n"
"border:1px solid #31AF91;}"))
        self.le_erosion_iterasyon.setObjectName(_fromUtf8("le_erosion_iterasyon"))
        self.label_49 = QtGui.QLabel(self.gb_erosion_gb)
        self.label_49.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.rb_erosion = QtGui.QRadioButton(self.gb_erosion_gb)
        self.rb_erosion.setGeometry(QtCore.QRect(20, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_erosion.setFont(font)
        self.rb_erosion.setObjectName(_fromUtf8("rb_erosion"))
        self.rb_dilation = QtGui.QRadioButton(self.gb_erosion_gb)
        self.rb_dilation.setGeometry(QtCore.QRect(120, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_dilation.setFont(font)
        self.rb_dilation.setStyleSheet(_fromUtf8(""))
        self.rb_dilation.setObjectName(_fromUtf8("rb_dilation"))
        self.pb_erosion_dilation = QtGui.QPushButton(self.gb_erosion_gb)
        self.pb_erosion_dilation.setGeometry(QtCore.QRect(20, 130, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_erosion_dilation.setFont(font)
        self.pb_erosion_dilation.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #247CB5;\n"
"color: #fff;\n"
"}"))
        self.pb_erosion_dilation.setObjectName(_fromUtf8("pb_erosion_dilation"))
        self.gv_erosion_result = QtGui.QGraphicsView(self.gb_erosion)
        self.gv_erosion_result.setGeometry(QtCore.QRect(780, 110, 350, 350))
        self.gv_erosion_result.setObjectName(_fromUtf8("gv_erosion_result"))
        self.gb_template = QtGui.QGroupBox(Dialog)
        self.gb_template.setGeometry(QtCore.QRect(150, 50, 1450, 700))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_template.setFont(font)
        self.gb_template.setStyleSheet(_fromUtf8("#gb_template{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_template::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #31AF91;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: #31AF91;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"color:#fff;\n"
"background-color:#31AF91;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"background-color:#31AF91;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #31AF91;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
""))
        self.gb_template.setObjectName(_fromUtf8("gb_template"))
        self.tabWidget_2 = QtGui.QTabWidget(self.gb_template)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 1481, 681))
        self.tabWidget_2.setStyleSheet(_fromUtf8("#tabWidget_2::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;}\n"
"#tabWidget_2::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"#tabWidget_2::tab {\n"
"    background: #31AF91;\n"
"    border: 2px solid #C4C4C3;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"color:#fff;\n"
"}\n"
"#tabWidget_2::tab:selected, QTabBar::tab:hover {\n"
"    background:#44F2C9;\n"
"}"))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pb_template_matching = QtGui.QPushButton(self.tab_5)
        self.pb_template_matching.setGeometry(QtCore.QRect(590, 300, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_template_matching.setFont(font)
        self.pb_template_matching.setStyleSheet(_fromUtf8("#pb_template_matching{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}\n"
"#pb_template_matching:hover{\n"
"background-color: #44F2C9;\n"
"color: #fff;\n"
"border-radius: 12px;\n"
"}"))
        self.pb_template_matching.setIconSize(QtCore.QSize(32, 32))
        self.pb_template_matching.setObjectName(_fromUtf8("pb_template_matching"))
        self.gv_parca = QtGui.QGraphicsView(self.tab_5)
        self.gv_parca.setGeometry(QtCore.QRect(590, 80, 200, 200))
        self.gv_parca.setObjectName(_fromUtf8("gv_parca"))
        self.label_10 = QtGui.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(590, 50, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gv_source = QtGui.QGraphicsView(self.tab_5)
        self.gv_source.setGeometry(QtCore.QRect(40, 80, 500, 500))
        self.gv_source.setObjectName(_fromUtf8("gv_source"))
        self.label_11 = QtGui.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(40, 35, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pb_upload_img = QtGui.QPushButton(self.tab_5)
        self.pb_upload_img.setGeometry(QtCore.QRect(490, 30, 48, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_upload_img.setFont(font)
        self.pb_upload_img.setStyleSheet(_fromUtf8("#pb_upload_img{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_upload_img:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_upload_img.setText(_fromUtf8(""))
        self.pb_upload_img.setObjectName(_fromUtf8("pb_upload_img"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.scrollArea = QtGui.QScrollArea(self.tab_6)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1450, 691))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollArea.setFont(font)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1462, 1650))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1462, 1481))
        self.scrollAreaWidgetContents.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scrollAreaWidgetContents.setAcceptDrops(True)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(20, 1360, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(20, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gv_cv1 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv1.setGeometry(QtCore.QRect(286, 90, 256, 192))
        self.gv_cv1.setObjectName(_fromUtf8("gv_cv1"))
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(20, 840, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gv_cv6 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv6.setGeometry(QtCore.QRect(286, 1410, 256, 192))
        self.gv_cv6.setObjectName(_fromUtf8("gv_cv6"))
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(20, 580, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gv_cv5 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv5.setGeometry(QtCore.QRect(286, 1150, 256, 192))
        self.gv_cv5.setObjectName(_fromUtf8("gv_cv5"))
        self.gv_cv2 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv2.setGeometry(QtCore.QRect(286, 370, 256, 192))
        self.gv_cv2.setObjectName(_fromUtf8("gv_cv2"))
        self.gv_cv3 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv3.setGeometry(QtCore.QRect(286, 630, 256, 192))
        self.gv_cv3.setObjectName(_fromUtf8("gv_cv3"))
        self.gv_cv4 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_cv4.setGeometry(QtCore.QRect(286, 890, 256, 192))
        self.gv_cv4.setObjectName(_fromUtf8("gv_cv4"))
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(20, 1100, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setGeometry(QtCore.QRect(20, 320, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(30, 870, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setGeometry(QtCore.QRect(30, 70, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setGeometry(QtCore.QRect(30, 350, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setGeometry(QtCore.QRect(30, 610, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gv_mr1 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr1.setGeometry(QtCore.QRect(30, 90, 256, 192))
        self.gv_mr1.setObjectName(_fromUtf8("gv_mr1"))
        self.gv_mr2 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr2.setGeometry(QtCore.QRect(30, 370, 256, 192))
        self.gv_mr2.setObjectName(_fromUtf8("gv_mr2"))
        self.gv_mr3 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr3.setGeometry(QtCore.QRect(30, 630, 256, 192))
        self.gv_mr3.setObjectName(_fromUtf8("gv_mr3"))
        self.gv_mr4 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr4.setGeometry(QtCore.QRect(30, 890, 256, 192))
        self.gv_mr4.setObjectName(_fromUtf8("gv_mr4"))
        self.label_23 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setGeometry(QtCore.QRect(30, 1130, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gv_mr5 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr5.setGeometry(QtCore.QRect(30, 1150, 256, 192))
        self.gv_mr5.setObjectName(_fromUtf8("gv_mr5"))
        self.label_24 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setGeometry(QtCore.QRect(30, 1390, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gv_mr6 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_mr6.setGeometry(QtCore.QRect(30, 1410, 256, 192))
        self.gv_mr6.setObjectName(_fromUtf8("gv_mr6"))
        self.label_25 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setGeometry(QtCore.QRect(286, 1390, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setGeometry(QtCore.QRect(286, 1130, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setGeometry(QtCore.QRect(286, 870, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setGeometry(QtCore.QRect(286, 610, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setGeometry(QtCore.QRect(286, 350, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setGeometry(QtCore.QRect(286, 70, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gv_r1 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r1.setGeometry(QtCore.QRect(644, 90, 256, 192))
        self.gv_r1.setObjectName(_fromUtf8("gv_r1"))
        self.gv_b1 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b1.setGeometry(QtCore.QRect(900, 90, 256, 192))
        self.gv_b1.setObjectName(_fromUtf8("gv_b1"))
        self.gv_r2 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r2.setGeometry(QtCore.QRect(644, 370, 256, 192))
        self.gv_r2.setObjectName(_fromUtf8("gv_r2"))
        self.gv_b2 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b2.setGeometry(QtCore.QRect(900, 370, 256, 192))
        self.gv_b2.setObjectName(_fromUtf8("gv_b2"))
        self.gv_r3 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r3.setGeometry(QtCore.QRect(644, 630, 256, 192))
        self.gv_r3.setObjectName(_fromUtf8("gv_r3"))
        self.gv_b3 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b3.setGeometry(QtCore.QRect(900, 630, 256, 192))
        self.gv_b3.setObjectName(_fromUtf8("gv_b3"))
        self.gv_r4 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r4.setGeometry(QtCore.QRect(644, 890, 256, 192))
        self.gv_r4.setObjectName(_fromUtf8("gv_r4"))
        self.gv_b4 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b4.setGeometry(QtCore.QRect(900, 890, 256, 192))
        self.gv_b4.setObjectName(_fromUtf8("gv_b4"))
        self.gv_r5 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r5.setGeometry(QtCore.QRect(644, 1150, 256, 192))
        self.gv_r5.setObjectName(_fromUtf8("gv_r5"))
        self.gv_b5 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b5.setGeometry(QtCore.QRect(900, 1150, 256, 192))
        self.gv_b5.setObjectName(_fromUtf8("gv_b5"))
        self.gv_r6 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_r6.setGeometry(QtCore.QRect(644, 1410, 256, 192))
        self.gv_r6.setObjectName(_fromUtf8("gv_r6"))
        self.gv_b6 = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        self.gv_b6.setGeometry(QtCore.QRect(900, 1410, 256, 192))
        self.gv_b6.setObjectName(_fromUtf8("gv_b6"))
        self.label_31 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setGeometry(QtCore.QRect(650, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setGeometry(QtCore.QRect(650, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setGeometry(QtCore.QRect(650, 610, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setGeometry(QtCore.QRect(650, 870, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setGeometry(QtCore.QRect(650, 1130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setGeometry(QtCore.QRect(650, 1390, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setGeometry(QtCore.QRect(900, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_38 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setGeometry(QtCore.QRect(900, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setGeometry(QtCore.QRect(900, 610, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setGeometry(QtCore.QRect(900, 870, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setGeometry(QtCore.QRect(900, 1130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_42 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setGeometry(QtCore.QRect(900, 1390, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setGeometry(QtCore.QRect(1230, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.lb_mse1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse1.setGeometry(QtCore.QRect(1230, 110, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse1.setFont(font)
        self.lb_mse1.setObjectName(_fromUtf8("lb_mse1"))
        self.lb_ssim1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim1.setGeometry(QtCore.QRect(1230, 140, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim1.setFont(font)
        self.lb_ssim1.setObjectName(_fromUtf8("lb_ssim1"))
        self.lb_ssim2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim2.setGeometry(QtCore.QRect(1230, 420, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim2.setFont(font)
        self.lb_ssim2.setObjectName(_fromUtf8("lb_ssim2"))
        self.lb_mse2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse2.setGeometry(QtCore.QRect(1230, 390, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse2.setFont(font)
        self.lb_mse2.setObjectName(_fromUtf8("lb_mse2"))
        self.label_48 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_48.setGeometry(QtCore.QRect(1230, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.lb_ssim3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim3.setGeometry(QtCore.QRect(1230, 680, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim3.setFont(font)
        self.lb_ssim3.setObjectName(_fromUtf8("lb_ssim3"))
        self.lb_mse3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse3.setGeometry(QtCore.QRect(1230, 650, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse3.setFont(font)
        self.lb_mse3.setObjectName(_fromUtf8("lb_mse3"))
        self.label_51 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_51.setGeometry(QtCore.QRect(1230, 610, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.lb_ssim4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim4.setGeometry(QtCore.QRect(1230, 940, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim4.setFont(font)
        self.lb_ssim4.setObjectName(_fromUtf8("lb_ssim4"))
        self.lb_mse4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse4.setGeometry(QtCore.QRect(1230, 910, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse4.setFont(font)
        self.lb_mse4.setObjectName(_fromUtf8("lb_mse4"))
        self.label_54 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_54.setGeometry(QtCore.QRect(1230, 870, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.lb_ssim5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim5.setGeometry(QtCore.QRect(1230, 1200, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim5.setFont(font)
        self.lb_ssim5.setObjectName(_fromUtf8("lb_ssim5"))
        self.lb_mse5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse5.setGeometry(QtCore.QRect(1230, 1170, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse5.setFont(font)
        self.lb_mse5.setObjectName(_fromUtf8("lb_mse5"))
        self.label_57 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_57.setGeometry(QtCore.QRect(1230, 1130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.lb_ssim6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_ssim6.setGeometry(QtCore.QRect(1230, 1460, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ssim6.setFont(font)
        self.lb_ssim6.setObjectName(_fromUtf8("lb_ssim6"))
        self.lb_mse6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_mse6.setGeometry(QtCore.QRect(1230, 1430, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mse6.setFont(font)
        self.lb_mse6.setObjectName(_fromUtf8("lb_mse6"))
        self.label_60 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_60.setGeometry(QtCore.QRect(1230, 1390, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.lb_psnr1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr1.setGeometry(QtCore.QRect(1230, 170, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr1.setFont(font)
        self.lb_psnr1.setObjectName(_fromUtf8("lb_psnr1"))
        self.lb_psnr2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr2.setGeometry(QtCore.QRect(1230, 450, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr2.setFont(font)
        self.lb_psnr2.setObjectName(_fromUtf8("lb_psnr2"))
        self.lb_psnr3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr3.setGeometry(QtCore.QRect(1230, 710, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr3.setFont(font)
        self.lb_psnr3.setObjectName(_fromUtf8("lb_psnr3"))
        self.lb_psnr4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr4.setGeometry(QtCore.QRect(1230, 970, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr4.setFont(font)
        self.lb_psnr4.setObjectName(_fromUtf8("lb_psnr4"))
        self.lb_psnr5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr5.setGeometry(QtCore.QRect(1230, 1230, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr5.setFont(font)
        self.lb_psnr5.setObjectName(_fromUtf8("lb_psnr5"))
        self.lb_psnr6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lb_psnr6.setGeometry(QtCore.QRect(1230, 1490, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_psnr6.setFont(font)
        self.lb_psnr6.setObjectName(_fromUtf8("lb_psnr6"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.gb_face_detection = QtGui.QGroupBox(Dialog)
        self.gb_face_detection.setGeometry(QtCore.QRect(150, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gb_face_detection.setFont(font)
        self.gb_face_detection.setStyleSheet(_fromUtf8("#gb_face_detection{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_face_detection::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
""))
        self.gb_face_detection.setObjectName(_fromUtf8("gb_face_detection"))
        self.gv_facedetection_source = QtGui.QGraphicsView(self.gb_face_detection)
        self.gv_facedetection_source.setGeometry(QtCore.QRect(20, 80, 550, 500))
        self.gv_facedetection_source.setObjectName(_fromUtf8("gv_facedetection_source"))
        self.pb_facedetection_upload_image = QtGui.QPushButton(self.gb_face_detection)
        self.pb_facedetection_upload_image.setGeometry(QtCore.QRect(520, 20, 48, 48))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_facedetection_upload_image.setFont(font)
        self.pb_facedetection_upload_image.setStyleSheet(_fromUtf8("#pb_facedetection_upload_image{\n"
"color: grey;\n"
"            border-image: url(./icons/open_image.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_facedetection_upload_image:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/open_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_facedetection_upload_image.setText(_fromUtf8(""))
        self.pb_facedetection_upload_image.setObjectName(_fromUtf8("pb_facedetection_upload_image"))
        self.pb_face_detection = QtGui.QPushButton(self.gb_face_detection)
        self.pb_face_detection.setGeometry(QtCore.QRect(20, 590, 550, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_face_detection.setFont(font)
        self.pb_face_detection.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #247CB5;\n"
"color: #fff;\n"
"}"))
        self.pb_face_detection.setObjectName(_fromUtf8("pb_face_detection"))
        self.groupBox_4 = QtGui.QGroupBox(self.gb_face_detection)
        self.groupBox_4.setGeometry(QtCore.QRect(650, 30, 781, 601))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox{\n"
"background-color: white;\n"
"text-align:center;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #31AF91;\n"
"}\n"
"QListWidget{color:#31AF91;\n"
"border:1px solid #31AF91;}"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.dateEdit = QtGui.QDateEdit(self.groupBox_4)
        self.dateEdit.setGeometry(QtCore.QRect(420, 50, 101, 22))
        self.dateEdit.setDate(QtCore.QDate(2018, 1, 11))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.tbl_devamsizlik = QtGui.QTableWidget(self.groupBox_4)
        self.tbl_devamsizlik.setGeometry(QtCore.QRect(10, 370, 551, 192))
        self.tbl_devamsizlik.setObjectName(_fromUtf8("tbl_devamsizlik"))
        self.tbl_devamsizlik.setColumnCount(0)
        self.tbl_devamsizlik.setRowCount(0)
        self.list_ogrenci = QtGui.QListWidget(self.groupBox_4)
        self.list_ogrenci.setGeometry(QtCore.QRect(240, 50, 150, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.list_ogrenci.setFont(font)
        self.list_ogrenci.setStyleSheet(_fromUtf8(""))
        self.list_ogrenci.setObjectName(_fromUtf8("list_ogrenci"))
        self.list_tum_ogrenci = QtGui.QListWidget(self.groupBox_4)
        self.list_tum_ogrenci.setGeometry(QtCore.QRect(50, 50, 150, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.list_tum_ogrenci.setFont(font)
        self.list_tum_ogrenci.setObjectName(_fromUtf8("list_tum_ogrenci"))
        item = QtGui.QListWidgetItem()
        self.list_tum_ogrenci.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_tum_ogrenci.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_tum_ogrenci.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_tum_ogrenci.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_tum_ogrenci.addItem(item)
        self.label_50 = QtGui.QLabel(self.groupBox_4)
        self.label_50.setGeometry(QtCore.QRect(50, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_52 = QtGui.QLabel(self.groupBox_4)
        self.label_52.setGeometry(QtCore.QRect(240, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.groupBox_4)
        self.label_53.setGeometry(QtCore.QRect(10, 340, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_55 = QtGui.QLabel(self.groupBox_4)
        self.label_55.setGeometry(QtCore.QRect(420, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.timeEdit = QtGui.QTimeEdit(self.groupBox_4)
        self.timeEdit.setGeometry(QtCore.QRect(420, 100, 118, 22))
        self.timeEdit.setTime(QtCore.QTime(9, 0, 0))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.label_56 = QtGui.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(420, 80, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.pb_fd_yoklama = QtGui.QPushButton(self.groupBox_4)
        self.pb_fd_yoklama.setGeometry(QtCore.QRect(420, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_fd_yoklama.setFont(font)
        self.pb_fd_yoklama.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #31AF91;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #247CB5;\n"
"color: #fff;\n"
"}"))
        self.pb_fd_yoklama.setObjectName(_fromUtf8("pb_fd_yoklama"))

        self.retranslateUi(Dialog)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "134410010 Bedirhan Sağlam Görüntü İşleme Ödev", None))
        self.pb_menu_1.setText(_translate("Dialog", "Temel İşlemler", None))
        self.pb_menu_2.setText(_translate("Dialog", "Mantıksal İşlemler", None))
        self.pb_menu_3.setText(_translate("Dialog", "Etiketleme", None))
        self.pb_menu_4.setText(_translate("Dialog", "Gürültü Oluşturma", None))
        self.pb_menu_5.setText(_translate("Dialog", "Erosion", None))
        self.pb_menu_6.setText(_translate("Dialog", "Şablon Eşleme", None))
        self.pb_menu_7.setText(_translate("Dialog", "Yüz Tanıma", None))
        self.gb_temel_islemler.setTitle(_translate("Dialog", "TEMEL İŞLEMLER", None))
        self.label.setText(_translate("Dialog", "Orijinal :", None))
        self.t1_resim_yukle.setToolTip(_translate("Dialog", "Görüntü Yükle", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Resmi Yeniden Boyutlandır", None))
        self.t1_pb_resize.setText(_translate("Dialog", "Tamam", None))
        self.label_3.setText(_translate("Dialog", "Width :", None))
        self.label_4.setText(_translate("Dialog", "Height :", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Resmi Döndür", None))
        self.t1_hs_lbl.setText(_translate("Dialog", "0", None))
        self.t1_pb_binary.setText(_translate("Dialog", "Binary Çevir", None))
        self.t1_pb_gray.setText(_translate("Dialog", "Griye Çevir", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("Dialog", "Temel İşlemler", None))
        self.t1_pb_sobel.setText(_translate("Dialog", "Sobel ", None))
        self.t1_pb_canny.setText(_translate("Dialog", "Canny Edges", None))
        self.t1_pb_prewitt.setText(_translate("Dialog", "Prewitt", None))
        self.t1_pb_threshold.setText(_translate("Dialog", "Threshold", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("Dialog", "Kenar Algılama", None))
        self.t1_pb_histogram.setText(_translate("Dialog", "Histogram Eşitle", None))
        self.lbl_hist_ssim.setText(_translate("Dialog", "SSIM :", None))
        self.label_45.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lbl_hist_mse.setText(_translate("Dialog", "MSE   :", None))
        self.label_46.setText(_translate("Dialog", "Önce :", None))
        self.label_47.setText(_translate("Dialog", "Sonra :", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("Dialog", "Histogram Eşitleme", None))
        self.label_2.setText(_translate("Dialog", "Sonuç :", None))
        self.t1_pb_menu.setToolTip(_translate("Dialog", "<html><head/><body><p>Menüyü Göster/Gizle</p></body></html>", None))
        self.pb_exit.setToolTip(_translate("Dialog", "Çıkış", None))
        self.pb_main_menu.setToolTip(_translate("Dialog", "Menü", None))
        self.gb_mantiksal_islemler.setTitle(_translate("Dialog", "MANTIKSAL İŞLEMLER", None))
        self.label_8.setText(_translate("Dialog", "Mantıksal İşlem :", None))
        self.t2_cb_mantiksal.setItemText(0, _translate("Dialog", "NOT", None))
        self.t2_cb_mantiksal.setItemText(1, _translate("Dialog", "AND", None))
        self.t2_cb_mantiksal.setItemText(2, _translate("Dialog", "OR", None))
        self.t2_cb_mantiksal.setItemText(3, _translate("Dialog", "AND NOT", None))
        self.t2_cb_mantiksal.setItemText(4, _translate("Dialog", "XOR", None))
        self.label_7.setText(_translate("Dialog", "Sonuç", None))
        self.label_5.setText(_translate("Dialog", "Görüntü A", None))
        self.label_6.setText(_translate("Dialog", "Görüntü B", None))
        self.gb_labeling.setTitle(_translate("Dialog", "ETİKETLEME", None))
        self.label_9.setText(_translate("Dialog", "Oluşan Şekiller :", None))
        self.t3_pb_labeling.setText(_translate("Dialog", "LABELİNG", None))
        self.t3_pb_tahmin.setText(_translate("Dialog", "Tahmin Et", None))
        self.gb_gurultu_olustur.setTitle(_translate("Dialog", "GÜRÜLTÜ OLUŞTURMA", None))
        self.label_44.setText(_translate("Dialog", "Gürültü Oranı :", None))
        self.lbl_slider.setText(_translate("Dialog", "0", None))
        self.pb_gurultu_olustur.setText(_translate("Dialog", "Gürültü Oluştur", None))
        self.gb_erosion.setTitle(_translate("Dialog", "EROSİON AND DİLATİON", None))
        self.label_49.setText(_translate("Dialog", "İterasyon Sayısı:", None))
        self.rb_erosion.setText(_translate("Dialog", "Erosion", None))
        self.rb_dilation.setText(_translate("Dialog", "Dilation", None))
        self.pb_erosion_dilation.setText(_translate("Dialog", "UYGULA", None))
        self.gb_template.setTitle(_translate("Dialog", "ŞABLON EŞLEME", None))
        self.pb_template_matching.setText(_translate("Dialog", "Template Matching", None))
        self.label_10.setText(_translate("Dialog", "Aranacak Parça :", None))
        self.label_11.setText(_translate("Dialog", "Kaynak resim", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Dialog", "Template Matching", None))
        self.label_14.setText(_translate("Dialog", "cv2.TM_SQDIFF_NORMED :", None))
        self.label_17.setText(_translate("Dialog", "cv2.TM_CCOEFF :", None))
        self.label_16.setText(_translate("Dialog", "cv2.TM_CCORR_NORMED :", None))
        self.label_12.setText(_translate("Dialog", "cv2.TM_CCORR :", None))
        self.label_18.setText(_translate("Dialog", "cv2.TM_SQDIFF :", None))
        self.label_15.setText(_translate("Dialog", "SONUÇLAR :", None))
        self.label_13.setText(_translate("Dialog", "cv2.TM_CCOEFF_NORMED:", None))
        self.label_19.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_20.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_21.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_22.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_23.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_24.setText(_translate("Dialog", "Eşleşen Sonuç (Matching Result) :", None))
        self.label_25.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_26.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_27.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_28.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_29.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_30.setText(_translate("Dialog", "Algılanan Nokta (Detected Point) :", None))
        self.label_31.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_32.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_33.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_34.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_35.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_36.setText(_translate("Dialog", "Aranan Parça :", None))
        self.label_37.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_38.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_39.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_40.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_41.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_42.setText(_translate("Dialog", "Bulunan Parça :", None))
        self.label_43.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_mse1.setText(_translate("Dialog", "MSE   :", None))
        self.lb_ssim1.setText(_translate("Dialog", "SSIM :", None))
        self.lb_ssim2.setText(_translate("Dialog", "SSIM :", None))
        self.lb_mse2.setText(_translate("Dialog", "MSE   :", None))
        self.label_48.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_ssim3.setText(_translate("Dialog", "SSIM :", None))
        self.lb_mse3.setText(_translate("Dialog", "MSE   :", None))
        self.label_51.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_ssim4.setText(_translate("Dialog", "SSIM :", None))
        self.lb_mse4.setText(_translate("Dialog", "MSE   :", None))
        self.label_54.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_ssim5.setText(_translate("Dialog", "SSIM :", None))
        self.lb_mse5.setText(_translate("Dialog", "MSE   :", None))
        self.label_57.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_ssim6.setText(_translate("Dialog", "SSIM :", None))
        self.lb_mse6.setText(_translate("Dialog", "MSE   :", None))
        self.label_60.setText(_translate("Dialog", "Benzerlik Oranı", None))
        self.lb_psnr1.setText(_translate("Dialog", "PSNR :", None))
        self.lb_psnr2.setText(_translate("Dialog", "PSNR :", None))
        self.lb_psnr3.setText(_translate("Dialog", "PSNR :", None))
        self.lb_psnr4.setText(_translate("Dialog", "PSNR :", None))
        self.lb_psnr5.setText(_translate("Dialog", "PSNR :", None))
        self.lb_psnr6.setText(_translate("Dialog", "PSNR :", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Dialog", "Sonuclar", None))
        self.gb_face_detection.setTitle(_translate("Dialog", "YÜZ TANIMA", None))
        self.pb_face_detection.setText(_translate("Dialog", "Yüzleri Algıla", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Devamsızlık Bilgisi", None))
        __sortingEnabled = self.list_tum_ogrenci.isSortingEnabled()
        self.list_tum_ogrenci.setSortingEnabled(False)
        item = self.list_tum_ogrenci.item(0)
        item.setText(_translate("Dialog", "Gilfoyle", None))
        item = self.list_tum_ogrenci.item(1)
        item.setText(_translate("Dialog", "Richard", None))
        item = self.list_tum_ogrenci.item(2)
        item.setText(_translate("Dialog", "Dinesh", None))
        item = self.list_tum_ogrenci.item(3)
        item.setText(_translate("Dialog", "Jared", None))
        item = self.list_tum_ogrenci.item(4)
        item.setText(_translate("Dialog", "Erlich", None))
        self.list_tum_ogrenci.setSortingEnabled(__sortingEnabled)
        self.label_50.setText(_translate("Dialog", "Tüm Öğrenciler :", None))
        self.label_52.setText(_translate("Dialog", "Gelen Öğrenciler :", None))
        self.label_53.setText(_translate("Dialog", "Devamsızlık Bilgisi :", None))
        self.label_55.setText(_translate("Dialog", "Tarih (GG/AA/YYYY) :", None))
        self.label_56.setText(_translate("Dialog", "Saat  :", None))
        self.pb_fd_yoklama.setText(_translate("Dialog", "Yoklama Al", None))

