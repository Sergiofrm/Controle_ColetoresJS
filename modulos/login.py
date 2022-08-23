
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton)
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import (QtCore,QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence,QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


#***************** Chamadas das Telas *************************

from template.login import Ui_Login
from modulos.principal import menu
from db.query import sqlite_db



class login(QMainWindow):
    
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.lineEdit_password.returnPressed.connect(self.ui.pushButton_login.click)
        self.ui.pushButton_login.setShortcut(QKeySequence("Enter"))
        self.showMaximized()
        
        # Icone de Tela de Login
        
        self.setWindowIcon(QIcon("icons/logi.png")) 
        
    def checkar_login(self,user,passwd):
        try:
            db = sqlite_db("sistema.db")
            lista = db.pega_dados("SELECT* FROM user")
            
            for row in lista:
                        if row [1].upper() == user.upper() and row[2] == passwd and row[4] == "Administrador":
                            return "Administrador"
                        if row [1].upper() == user.upper() and row[2] == passwd and row[4] == "Usuário":
                            return "Usuário"
                        else:
                            continue
            return "Sem Acesso"  
        
        except:
            pass
        
    def login(self):
        
        db = sqlite_db("sistema.db")
        
        user = self.ui.lineEdit_user.text()
        passwd = self.ui.lineEdit_password.text()
        self.checkar_login(user,passwd)
        # Buscar o Perfil no Banco de Dados
        
        perfil = self.checkar_login(user.upper(),passwd)
       
        
        if user == "" or passwd == "":
            
            QMessageBox.warning(QMessageBox(),"Alerta!", "Prencha todos os campos!!")
            
        else:
            
            dados = db.pega_dados("SELECT acesso FROM user WHERE nome = '{}' and senha = '{}'".format(user,passwd))
            
            if dados:
                
                self.logado = user
                QMessageBox.information(QMessageBox(),"Login realizado!","Usuário Logado com sucesso!!\n" "Seja bem vindo(a), "+str(user.upper()))
                self.window = menu(self,self.logado,perfil)
                self.window.show() 
                self.hide()
                
            
            else:
                QMessageBox.warning(QMessageBox(),"Login errado!","Usuário e Senha incorreta")
                
        

            
                 
 
app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login()
    window.show()
    
sys.exit(app.exec_())