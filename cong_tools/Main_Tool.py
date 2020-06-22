# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Tools.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Common.log import mylog
import os
import time
import subprocess
import mapallpath
import threadinfo


class EmittingStream(QtCore.QObject):
    # 定义一个发送str的信号
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(910, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(910, 640))
        mainWindow.setMaximumSize(QtCore.QSize(910, 640))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 891, 351))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.pushButton_2.setMinimumSize(QtCore.QSize(111, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/123/ut/res/image/input.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 70, 111, 41))
        self.pushButton_4.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 20, 111, 41))
        self.pushButton_5.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 70, 111, 41))
        self.pushButton_6.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 70, 111, 41))
        self.pushButton_7.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 20, 111, 41))
        self.pushButton_10.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(170, 120, 231, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 30, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 120, 141, 111))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 20, 121, 23))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 50, 121, 23))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 80, 121, 23))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(260, 20, 111, 41))
        self.pushButton_15.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 240, 141, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 62, 121, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 200, 61, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(180, 240, 211, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(180, 270, 211, 22))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(480, 150, 61, 51))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_20.setGeometry(QtCore.QRect(480, 250, 61, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_22.setGeometry(QtCore.QRect(380, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_23.setGeometry(QtCore.QRect(380, 70, 101, 41))
        self.pushButton_23.setObjectName("pushButton_23")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(610, 20, 271, 321))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 251, 291))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 380, 891, 211))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(-1, -1, 891, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.pushButton_2, self.pushButton_4)
        mainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        mainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        mainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "个人工具"))
        self.groupBox_2.setTitle(_translate("mainWindow", "功能区"))
        self.pushButton_2.setToolTip(_translate("mainWindow", "车机点火"))
        self.pushButton_2.setText(_translate("mainWindow", "车机点火"))
        self.pushButton_4.setToolTip(_translate("mainWindow", "车机熄火"))
        self.pushButton_4.setText(_translate("mainWindow", "车机熄火"))
        self.pushButton_5.setToolTip(_translate("mainWindow", "Push文件"))
        self.pushButton_5.setText(_translate("mainWindow", "Push文件"))
        self.pushButton_6.setToolTip(_translate("mainWindow", "Pull文件"))
        self.pushButton_6.setText(_translate("mainWindow", "Pull文件"))
        self.pushButton_7.setToolTip(_translate("mainWindow", "下班回家打卡"))
        self.pushButton_7.setText(_translate("mainWindow", "下班回家打卡"))
        self.pushButton_10.setToolTip(_translate("mainWindow", "翻译"))
        self.pushButton_10.setText(_translate("mainWindow", "翻译"))
        self.groupBox_6.setTitle(_translate("mainWindow", "获取log"))
        self.checkBox.setText(_translate("mainWindow", "logcat"))
        self.checkBox_2.setText(_translate("mainWindow", "kernel"))
        self.pushButton.setToolTip(_translate("mainWindow", "确认"))
        self.pushButton.setText(_translate("mainWindow", "确认"))
        self.pushButton_3.setToolTip(_translate("mainWindow", "取消"))
        self.pushButton_3.setText(_translate("mainWindow", "取消"))
        self.groupBox_7.setTitle(_translate("mainWindow", "车机操作"))
        self.pushButton_11.setToolTip(_translate("mainWindow", "fastboot"))
        self.pushButton_11.setText(_translate("mainWindow", "fastboot"))
        self.pushButton_12.setToolTip(_translate("mainWindow", "recovery"))
        self.pushButton_12.setText(_translate("mainWindow", "recovery"))
        self.pushButton_17.setToolTip(_translate("mainWindow", "reboot"))
        self.pushButton_17.setText(_translate("mainWindow", "reboot"))
        self.pushButton_15.setToolTip(_translate("mainWindow", "查看系统V850和RL78版本号"))
        self.pushButton_15.setText(_translate("mainWindow", "车机截图"))
        self.pushButton_14.setToolTip(_translate("mainWindow", "环境切换"))
        self.pushButton_14.setText(_translate("mainWindow", "P环境 -> QA环境"))
        self.groupBox_3.setTitle(_translate("mainWindow", "六期地图激活"))
        self.pushButton_16.setToolTip(_translate("mainWindow", "地图激活1行"))
        self.pushButton_16.setText(_translate("mainWindow", "地图激活1行"))
        self.pushButton_18.setToolTip(_translate("mainWindow", "地图激活2行"))
        self.pushButton_18.setText(_translate("mainWindow", "地图激活2行"))
        self.pushButton_8.setToolTip(_translate("mainWindow", "Home键"))
        self.pushButton_8.setText(_translate("mainWindow", "Home"))
        self.pushButton_13.setToolTip(_translate("mainWindow", "导出bootlog"))
        self.pushButton_13.setText(_translate("mainWindow", "导出bootlog"))
        self.comboBox.setItemText(0, _translate("mainWindow", "关闭模拟地图"))
        self.comboBox.setItemText(1, _translate("mainWindow", "激活模拟地图"))
        self.pushButton_19.setToolTip(_translate("mainWindow", "音量+"))
        self.pushButton_19.setText(_translate("mainWindow", "音量+"))
        self.pushButton_20.setToolTip(_translate("mainWindow", "音量-"))
        self.pushButton_20.setText(_translate("mainWindow", "音量-"))
        self.pushButton_22.setToolTip(_translate("mainWindow", "fastboot刷机"))
        self.pushButton_22.setText(_translate("mainWindow", "fastboot刷机"))
        self.pushButton_23.setText(_translate("mainWindow", "修改车机时间"))
        self.groupBox.setTitle(_translate("mainWindow", "车机信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "日志输出"))

        # 初始化相关命令
        self.Path = os.path.dirname(__file__)
        self.adb = 'adb -host shell'

        # 开多线程检测USB是否连接
        lt = [self.pushButton_16, self.pushButton_18, self.pushButton_13, self.pushButton_15, self.pushButton_14, \
              self.pushButton_5, self.pushButton_6, self.pushButton_2, self.pushButton_4, \
              self.pushButton_11, self.pushButton_12, self.pushButton_17, self.checkBox, \
              self.checkBox_2]
        for i in lt:
            i.setEnabled(False)
        self.ls = threadinfo.LookSystem(lt)
        self.bHThread = threadinfo.backHomeThread()
        self.BL = threadinfo.BootLog()
        self.FB = threadinfo.FastBoot()
        self.Rc = threadinfo.Recovery()
        self.Re = threadinfo.Reboot()
        self.lvr = threadinfo.LookV850Rl78()
        self.ls.start()

        # 点击触发信号
        self.pushButton_2.clicked.connect(self.ignition)
        self.pushButton_4.clicked.connect(self.Stalling)
        self.pushButton_5.clicked.connect(self.push)
        self.pushButton_6.clicked.connect(self.pull)
        self.pushButton_7.clicked.connect(self.backHome)
        self.pushButton_10.clicked.connect(self.bd_translate)
        self.pushButton_11.clicked.connect(self.fastboot)
        self.pushButton_12.clicked.connect(self.recovery)
        self.pushButton_17.clicked.connect(self.reboot)
        self.pushButton_13.clicked.connect(self.bootlog)
        self.checkBox.stateChanged.connect(self.get_logcat)
        self.checkBox_2.stateChanged.connect(self.get_kernel)
        self.pushButton_16.clicked.connect(self.map_one)
        self.pushButton_18.clicked.connect(self.map_two)
        self.pushButton_15.clicked.connect(self.look_v850_rl78)
        self.pushButton_14.clicked.connect(self.change_environ)
        self.pushButton.clicked.connect(self.get_logcat_info)
        self.pushButton.clicked.connect(self.get_kernel_info)
        self.pushButton_3.clicked.connect(self.stop_alllog_info)
        self.pushButton_3.setEnabled(False)

        # 重定向输出
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    # 退出窗口的二次确认界面
    # 英文版本
    '''
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
        "确定退出吗？", QtWidgets.QMessageBox.Yes |
        QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''

    # 退出窗口的二次确认界面
    # 中文版本
    def closeEvent(self, event):
        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle('退出')
        msgBox.setText('确定退出吗？')
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        cbtn = msgBox.addButton('确认', QtWidgets.QMessageBox.ActionRole)
        abtn = msgBox.addButton('取消', QtWidgets.QMessageBox.ActionRole)
        msgBox.exec_()
        # if msgBox.clickedButton() == cbtn:
        #     event.accept()
        # elif msgBox.clickedButton() == abtn:
        #     event.ignore()
        # else:
        #     sys.exit(msgBox.exec_())

    def ignition(self):
        # 调用log模块
        logger = mylog('ignition', self.Path).getlog()
        logger.info('你点击了车机点火')
        os.system(r'adb -host shell "dbus-send --system --type=signal /com/saic/ivi/CarService com.saic.ivi.CarService.PowerStatus string:\"{\\\"sigVal\\\":\\\"2\\\"}\""')
        logger.handlers.clear()

    def Stalling(self):
        logger = mylog('Stalling', self.Path).getlog()
        logger.info('你点击了车机熄火')
        os.system(r'adb -host shell "dbus-send --system --type=signal /com/saic/ivi/CarService com.saic.ivi.CarService.PowerStatus string:\"{\\\"sigVal\\\":\\\"0\\\"}\""')
        logger.handlers.clear()

    def push(self):
        logger = mylog('push', self.Path).getlog()
        ps = subprocess.getoutput('adb -host push' + ' ' + self.Path + '/files/DEL.txt' + ' ' + 'lib')
        logger.info('已push文件---速度为：' + ps)
        logger.handlers.clear()

    def pull(self):
        logger = mylog('pull', self.Path).getlog()
        pl = subprocess.getoutput('adb -host pull' + ' ' + 'lib/DEL.txt' + ' ' + self.Path + '/files')
        logger.info('已pull文件---速度为：' + pl)
        logger.handlers.clear()

    def backHome(self):
        logger = mylog('backHome', self.Path).getlog()
        logger.info('我下班回家了，正在打开打卡网页...')
        self.bHThread.start()
        logger.handlers.clear()

    def map_one(self):
        # 初始化数据
        # 实例化对象调用返回的数据
        ma = mapallpath.MapPath().get_info()
        mo = threadinfo.MapOneThread(ma[0], ma[1])
        logger = mylog('map_one', self.Path).getlog()
        logger.info('正在输入第一行密钥...')
        mo.start()
        logger.handlers.clear()

    def map_two(self):
        # 初始化数据
        # 实例化对象调用返回的数据
        ma = mapallpath.MapPath().get_info()
        mt = threadinfo.MapTwoThread(ma[0], ma[1])
        logger = mylog('map_two', self.Path).getlog()
        logger.info('正在输入第二行密钥...')
        mt.start()
        logger.handlers.clear()

    def bd_translate(self):
        logger = mylog('bd_translate', self.Path).getlog()
        logger.info('打开翻译......')
        logger.handlers.clear()

    def look_v850_rl78(self):
        logger = mylog('look_v850_rl78', self.Path).getlog()
        logger.info('正在查看......')
        self.lvr.start()
        logger.handlers.clear()

    # 切换环境
    def change_environ(self):
        logger = mylog('change_environ', self.Path).getlog()
        logger.info('正在从P环境本切换成E环境......')
        logger.handlers.clear()

    def bootlog(self):
        logger = mylog('bootlog', self.Path).getlog()
        logger.info('正在抓取bootlog')
        self.BL.start()
        logger.handlers.clear()

    # 选中或者取消复选框打印信息
    def get_logcat(self):
        logger = mylog('get_logcat', self.Path).getlog()
        if self.checkBox.isChecked():
            logger.info('正在打开logcat......')
        else:
            logger.info('正在关闭logcat......')
        logger.handlers.clear()

    # 选中或者取消复选框打印信息
    def get_kernel(self):
        logger = mylog('get_kernel', self.Path).getlog()
        if self.checkBox_2.isChecked():
            logger.info('正在打开kernel......')
        else:
            logger.info('正在关闭kernel......')
        logger.handlers.clear()

    # 打印logcat信息
    def get_logcat_info(self):
        logger = mylog('get_logcat_info', self.Path).getlog()
        if self.checkBox.isChecked():
            logger.info('正在抓取logcat......')
            self.pushButton.setEnabled(False)
            self.pushButton_3.setEnabled(True)
            Time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            self.Folder = self.Path + '\\logs\\logs_{0}'.format(Time)
            # 创建文件夹，如果有就不创建
            if not os.path.exists(self.Folder):
                os.mkdir(self.Folder)
            with open('{0}\\logcat.log'.format(self.Folder), 'wb') as logcat:
                self.lc = subprocess.Popen(r'adb -host logcat -v time', shell=True, stdout=logcat)
        logger.handlers.clear()

    # 打印kernel信息
    def get_kernel_info(self):
        logger = mylog('get_kernel_info', self.Path).getlog()
        if self.checkBox_2.isChecked():
            logger.info('正在抓取kernel......')
            self.pushButton.setEnabled(False)
            self.pushButton_3.setEnabled(True)
            Time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            self.Folder = self.Path + '\\logs\\logs_{0}'.format(Time)
            # 创建文件夹，如果有就不创建
            if not os.path.exists(self.Folder):
                os.mkdir(self.Folder)
            with open('{0}\\kernel.log'.format(self.Folder), 'wb') as kernel:
                subprocess.Popen(r'adb -host shell dmesg', shell=True, stdout=kernel)
        logger.handlers.clear()

    # 关闭所有正在抓取的Log
    def stop_alllog_info(self):
        try:
            subprocess.getoutput("taskkill /F /T /PID " + str(self.lc.pid))
            subprocess.Popen(r'explorer {0}'.format(self.Folder))
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(False)
        except:
            subprocess.Popen(r'explorer {0}'.format(self.Folder))
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(False)

    def fastboot(self):
        logger = mylog('fastboot', self.Path).getlog()
        logger.info('正在进入fastboot模式......')
        self.FB.start()
        logger.handlers.clear()

    def recovery(self):
        logger = mylog('fastboot', self.Path).getlog()
        logger.info('正在进入recovery模式......')
        self.Rc.start()
        logger.handlers.clear()

    def reboot(self):
        logger = mylog('fastboot', self.Path).getlog()
        logger.info('正在重启车机.....')
        self.Re.start()
        logger.handlers.clear()

