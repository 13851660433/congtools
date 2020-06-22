# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Subtools.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from document import session
import sys


class EmittingStream(QtCore.QObject):
        # 定义一个发送str的信号
        textWritten = QtCore.pyqtSignal(str)

        def write(self, text):
            self.textWritten.emit(str(text))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 581, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(-1, -1, 581, 281))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "翻译器"))
        self.pushButton.setToolTip(_translate("Dialog", "翻译"))
        self.pushButton.setText(_translate("Dialog", "翻译"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入翻译的内容"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "翻译内容："))

        # 点击翻译按钮
        self.pushButton.clicked.connect(self.translate)

        # 重定向
        # sys.stderr = EmittingStream(textWritten=self.outputWritten)

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def translate(self):
        # 重定向
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        self.textEdit.clear()
        session.TranSlate(self.lineEdit.text())

