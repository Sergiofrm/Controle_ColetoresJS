Qmesnagem="""
QMessageBox{background-color: rgb(255, 59, 59);}
            QLabel{width:1990px 1200px ;font-size: 20px;color:rgb(245,245,245);}
            QPushButton{background-color: rgb(255, 255, 255);font: 87 20pt Segoue;}
            QPushButton:hover{background-color: rgb(215, 215, 215);opacity: 200;}
QMessageBox {
    border-radius: 2px;
    opacity: 100;
    border: 5px solid #ffffff;
     border-top-color : White; 
border-left-color :White;
border-right-color :White;
 border-bottom-color : White;                   
}

"""


################################################## Não Utilizada ########################



telaimprimir="""
QMainWindow {
    background: #002025;
    border-radius: 5px;
    opacity: 100;
    border: 2px solid #2c8484;}

}
"""

ENABLE_STYLESHEET = """
    QPushButton {
        border: 1px solid #007a94;
        border-radius: 6px;
        color:#ffffff;
        background-color: #007a94;
        
        }
    QPushButton:pressed {
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #008aa6, stop: 1 #008aa6);
        }

    QPushButton:flat {
        border: none;
        }
"""    
DISABLE_STYLESHEET = """
    QPushButton {
       border: 1px solid #808080;
       border-radius: 6px;
       color:#ffffff;
       background-color: #808080;
       
       }
   QPushButton:flat {
       border: none;
       }

"""
menubar= """
    QStatusBar{border: 0; background-color: #FFF8DC;

    }
    QStatusBar::item {border: none;}

"""