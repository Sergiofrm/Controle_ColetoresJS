from modulos.cadastrar import cadastrar
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton)
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import (QtCore,QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.menu import Ui_MainWindow
from modulos.cadastrar import cadastrar
from db.query import sqlite_db

class menu(QMainWindow):
    
    def __init__(self,telalogin,logado,perfil,*args,**argvs):
        super(menu,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.telalogin = telalogin
        self.showMaximized()
        self.ui.Btn_Toggle.clicked.connect(self.add) #Botão JS Solutions
        self.userlogado = logado
        self.ui.version.setStyleSheet("color: rgb(150, 150, 150);")
        self.ui.version.setText("Usuário :" +" "  +logado.upper())
        
        # Condição se o Usuário for Administrador:
        
        if not perfil =='Administrador':
            
            # Botões para Edição 
            
            self.ui.Btn_Toggle.setEnabled(False) # Somente Visivel
            self.ui.btn_page_1.setVisible(False) # Desaparece
            self.ui.btn_page_2.setVisible(False) # Desaparece
            self.ui.btn_page_3.setVisible(False) # Desaparece
            self.ui.btn_page_4.setVisible(False) # Desaparece            
            
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Atenção',
                                     "Tem certeza que deseja sair?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
            self.telalogin.show()
            self.clearMask()

 
        else:
            event.ignore()    
        
        
        
        
        
    def add(self):
        self.add = cadastrar()
        self.add.show()
    
  