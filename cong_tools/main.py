# coding=utf-8
__author__ = 'cong'

from Main_Tool import Ui_mainWindow
from Subtools import Ui_Dialog
from Version import Ui_Dialog1
from Chtime import Ui_Dialog2
from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


class SubWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.setupUi(self)


class Version(QtWidgets.QDialog, Ui_Dialog1):
    def __init__(self):
        super(Version, self).__init__()
        self.setupUi(self)


class Chtime(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self):
        super(Chtime, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    sw = SubWindow()
    vs = Version()
    ct = Chtime()
    ui.pushButton_10.clicked.connect(sw.show)
    ui.pushButton_14.clicked.connect(vs.show)
    ui.pushButton_23.clicked.connect(ct.show)
    ui.show()
    sys.exit(app.exec_())
