# coding=utf-8
__author__ = 'cong'


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os
from Common.log import mylog
import re
import xlrd
from document import BackHome


# 多线程启后调用此方法来检测USB连接状态
class LookSystem(QtCore.QThread):
    def __init__(self, *args, **kwargs):
        super(LookSystem, self).__init__()
        self.args = args

    def run(self):
        while True:
            cmd = r'adb -host shell "getprop | grep vin"'
            vn = subprocess.getoutput(cmd)
            # 判断设备连与不连时 按钮状态
            if vn == 'error: device not found':
                for i in self.args[0]:
                    i.setEnabled(False)
            else:
                for i in self.args[0]:
                    i.setEnabled(True)


class LookV850Rl78(QtCore.QThread):
    def __init__(self):
        super(LookV850Rl78, self).__init__()

    def run(self):
        pattern = r':(.*),'
        Path = os.path.dirname(__file__)
        cmd = r'adb -host shell "sys-test --get-ver"'
        logger = mylog('look_v850_rl78', Path).getlog()
        lvr = subprocess.getoutput(cmd)
        vr = re.findall(pattern, lvr)
        if len(vr) == 2:
            logger.info('\nV850:{0}\nRL78:{1}'.format(vr[0], vr[1]))
        elif len(vr) == 1:
            logger.info('\nV850:{0}\nRL78:{1}'.format(vr[0], 'None'))
        logger.handlers.clear()


class backHomeThread(QtCore.QThread):
    def __init__(self):
        super(backHomeThread, self).__init__()

    def run(self):
        Path = os.path.dirname(__file__)
        logger = mylog('backHome', Path).getlog()
        name = '周聪'
        job_name = 'wb-zc193433'
        company = '诚迈'
        project = '五菱'
        task = '测试用例及测试报告'
        url = 'https://www.aliwork.com/alibaba/web/APP_SEV4BNNJ6PPK40RBN3UN/inst/formSubmit.html?\
                formUuid=FORM-ZIYJ8JEVWTY4XCPCY2LF8SQ4IO1W1NS2WQXUJ7#/'
        try:
            home = BackHome.BackHome(url)
            home.name(name)
            home.job_number(job_name)
            home.date()
            home.company(company)
            home.project(project)
            home.task(task)
            home.quit()
            logger.info('我已打完卡，下班回家')
        except:
            logger.info('未打卡成功，不允许下班')
        logger.handlers.clear()


class MapOneThread(QtCore.QThread):
    def __init__(self, car, vin):
        super(MapOneThread, self).__init__()
        self.car = car
        self.vin = vin

    def run(self):
        row = 0
        adb = r'adb -host shell input text'
        Path = os.path.dirname(__file__)
        logger = mylog('map_one', Path).getlog()
        if 'C520' in self.car[0]:
            xo = xlrd.open_workbook(Path + '\\files\\C520.xlsx')
            sheet = xo.sheet_by_index(0)
            for i in sheet.col_values(6):
                row += 1
                if self.vin[0] == i:
                    ones = sheet.cell(row - 1, 2).value
                    # print(adb + " {0}".format(ones))
                    subprocess.getoutput(adb + " {0}".format(ones))
                    break
            logger.error('你的车机地图激活码没有......')

        elif 'CN210' in self.car[0]:
            xo1 = xlrd.open_workbook(Path + '\\files\\CN210S.xlsx')
            sheet1 = xo1.sheet_by_index(0)
            for i1 in sheet1.col_values(6):
                row += 1
                if self.vin[0] == i1:
                    ones1 = sheet1.cell(row - 1, 2).value
                    # print(adb + " {0}".format(ones))
                    subprocess.getoutput(adb + " {0}".format(ones1))
                    break
            logger.error('你的车机地图激活码没有......')

        else:
            logger.info('车机号：{0}不需要激活激活'.format(self.car[0]))
        logger.handlers.clear()


class MapTwoThread(QtCore.QThread):
    def __init__(self, car, vin):
        super(MapTwoThread, self).__init__()
        self.car = car
        self.vin = vin

    def run(self):
        row = 0
        adb = r'adb -host shell input text'
        Path = os.path.dirname(__file__)
        logger = mylog('map_two', Path).getlog()
        if 'C520' in self.car[0]:
            xo = xlrd.open_workbook(Path + '\\files\\C520.xlsx')
            sheet = xo.sheet_by_index(0)
            for i in sheet.col_values(6):
                row += 1
                if self.vin[0] == i:
                    ones = sheet.cell(row - 1, 3).value
                    # print(adb + " {0}".format(ones))
                    subprocess.getoutput(adb + " {0}".format(ones))
                    break
            logger.error('你的车机地图激活码没有......')

        elif 'CN210' in self.car[0]:
            xo1 = xlrd.open_workbook(Path + '\\files\\CN210S.xlsx')
            sheet1 = xo1.sheet_by_index(0)
            for i1 in sheet1.col_values(6):
                row += 1
                if self.vin[0] == i1:
                    ones1 = sheet1.cell(row - 1, 3).value
                    # print(adb + " {0}".format(ones))
                    subprocess.getoutput(adb + " {0}".format(ones1))
                    break
            logger.error('你的车机地图激活码没有......')

        else:
            logger.info('车机号：{0}不需要激活激活'.format(self.car[0]))
        logger.handlers.clear()


class BootLog(QtCore.QThread):
    def __init__(self):
        super(BootLog, self).__init__()

    def run(self):
        Path = os.path.dirname(__file__)
        os.system('adb -host pull' + ' ' + '/var/bootlog' + ' ' + Path + '/logs/bootlog')


class FastBoot(QtCore.QThread):
    def __init__(self):
        super(FastBoot, self).__init__()

    def run(self):
        os.system(r'adb -host shell "reboot -f fastboot"')


class Recovery(QtCore.QThread):
    def __init__(self):
        super(Recovery, self).__init__()

    def run(self):
        os.system(r'adb -host shell "reboot -f recovery"')


class Reboot(QtCore.QThread):
    def __init__(self):
        super(Reboot, self).__init__()

    def run(self):
        os.system('adb -host reboot')


class ChangeEnviron(QtCore.QThread):
    def __init__(self, vsi):
        super(ChangeEnviron, self).__init__()
        self.vsi = vsi

    def run(self):
        Path = os.path.dirname(__file__)
        logger = mylog('change_environ', Path).getlog()
        cmd = r'adb -host shell "mount -o remount rw /;sed -i "s/{0}P/{0}E/g" /usr/build.prop"'.format(self.vsi)
        logger.info(cmd)
        subprocess.getoutput(cmd)
