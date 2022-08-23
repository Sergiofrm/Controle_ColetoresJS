# Equipe Hacker

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from modulos.login import login


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login()
    window.show()
sys.exit(app.exec())


# Tela Princial - Acesso ao Coletor
