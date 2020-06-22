# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chtime.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(330, 60)
        Dialog2.setMinimumSize(QtCore.QSize(330, 60))
        Dialog2.setMaximumSize(QtCore.QSize(330, 60))
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 20, 221, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "修改车机时间"))
        self.pushButton.setToolTip(_translate("Dialog2", "修改"))
        self.pushButton.setText(_translate("Dialog2", "修改"))

        self.pushButton.clicked.connect(self.changtime)
        self.pushButton.clicked.connect(self.close)

    def changtime(self):
        cmd = 'adb -host shell "date --set \"{0}\""'.format(self.dateTimeEdit.text())
        print(cmd)
        # subprocess.getoutput()
