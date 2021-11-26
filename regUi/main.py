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
        
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = RegApp()
    Form.show()
    sys.exit(app.exec_())
