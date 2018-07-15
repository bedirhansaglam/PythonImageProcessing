# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:12:45 2017

@author: Bedirhan
"""

import sys
from PyQt4 import QtGui
from Main import MainWindow

def main():
    app=QtGui.QApplication(sys.argv)
    
    mainWindow=MainWindow()
    mainWindow.show()
    return app.exec_()
    
    

if __name__=="__main__":
    main()