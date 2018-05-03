# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:17:14 2015

@author: danaukes
"""

import os
import sys
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import PyQt5.QtWidgets as qw
#import numpy
#import numpy.linalg
#import scipy
#import scipy.optimize
#import scipy.linalg
#import scipy.integrate
#import scipy.integrate.vode
#from scipy.spatial import Delaunay
#import scipy.spatial.ckdtree
#import sympy

def build_main():
    main_window = MainWindow()
    widget = Widget()
    main_window.setCentralWidget(widget)
    return main_window
    
class MainWindow(qw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle('Test')
        menu   = self.menuBar().addMenu('File')
        action = menu.addAction('Action')
        action.triggered.connect(self.method)   
        
    def method(self):
#        pass
        d = Dialog()
        if d.exec_():
            print(True)
        
class Widget(qw.QWidget):
    def __init__(self,*args,**kwargs):
        super(Widget,self).__init__(*args,**kwargs)
        layout = qw.QHBoxLayout()
        layout.addWidget(qw.QLabel('Main Widget'))
        self.setLayout(layout)

class Dialog(qw.QDialog):
    def __init__(self,*args,**kwargs):
        super(Dialog,self).__init__(*args,**kwargs)
        self.b1 = qw.QPushButton('ok')
        self.b2 = qw.QPushButton('cancel')
        layout = qw.QHBoxLayout()
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        self.setLayout(layout)
        
        self.b1.clicked.connect(self.accept)
        self.b2.clicked.connect(self.reject)

if __name__=='__main__':
    
    app = qw.QApplication(sys.argv)
    main_window = build_main()
    main_window.show()
    sys.exit(app.exec_())
    