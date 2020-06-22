# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Version.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threadinfo


class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(320, 60)
        Dialog1.setMinimumSize(QtCore.QSize(320, 60))
        Dialog1.setMaximumSize(QtCore.QSize(320, 60))
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "版本"))
        self.pushButton.setToolTip(_translate("Dialog1", "确认"))
        self.pushButton.setText(_translate("Dialog1", "确认"))
        self.lineEdit.setPlaceholderText(_translate("Dialog1", "请输入版本号"))

        # 点击确认按钮
        self.pushButton.clicked.connect(self.changeenviron)
        self.pushButton.clicked.connect(self.close)

    def changeenviron(self):
        vsi = self.lineEdit.text()
        self.ce = threadinfo.ChangeEnviron(vsi)
        self.ce.start()

