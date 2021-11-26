######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################

from PyQt5 import QtWidgets, QtCore
from regUi import Ui_Form
import sys

class RegApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(RegApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = RegApp()
    Form.show()
    sys.exit(app.exec_())
