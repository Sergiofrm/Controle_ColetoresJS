
from typing import Text
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton)
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import (QtCore,QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

#***************** Chamadas das Telas *************************


from template.tela_cad import Ui_cadastrar
from db.query import sqlite_db

#***************** Classe Page Cadastrar *************************


class cadastrar(QMainWindow):
    
    def __init__(self,*args,**argvs):
        super(cadastrar,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar()
        self.ui.setupUi(self)
        self.showMaximized()
        self.ui.pushButton_login_2.clicked.connect(self.add)
        self.ui.pushButton_login_3.clicked.connect(self.can)
        
    def add(self):
        db = sqlite_db("sistema.db")
        
        name = self.ui.lineEdit_user.text()
        senh = self.ui.lineEdit_password.text()
        lid = self.ui.lineEdit_password_3.currentText()
        carg = self.ui.lineEdit_password_2.text()
        #adm = 1
        
        if name =="" or senh ==""or carg =="":
            QMessageBox.information(QMessageBox(),"Atenção!","Favor preencher todos os campos!")
        else:
            db.inserir_apaga_atualiza("INSERT INTO user (nome,senha,cargo,acesso) VALUES ('{}', '{}', '{}', '{}')".format(name,senh,carg,lid))
            QMessageBox.information(QMessageBox(),"Concluído!","Dados gravados com sucesso")
            
            # Botão de Limpeza depois de cadastrar
            
            self.ui.lineEdit_user.setText("")
            self.ui.lineEdit_password.setText("")
            self.ui.lineEdit_password_2.setText("")
            
            
                
    def can(self):
        self.close()
        
        