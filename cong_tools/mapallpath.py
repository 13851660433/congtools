# coding=utf-8
__author__ = 'cong'


import re
import subprocess


class MapPath(object):
    def __init__(self):
        cmd = r'adb -host shell "getprop | grep vin"'
        vn = subprocess.getoutput(cmd)
        pattern = r': \[(.*)\]'
        self.vin = re.findall(pattern, vn)
        cmdtwo = r'adb -host shell "getprop | grep version"'
        vntwo = subprocess.getoutput(cmdtwo)
        patterntwo = r'\[ro.zxq.release.version\]: \[(.*)\]'
        self.car = re.findall(patterntwo, vntwo)

    def get_info(self):
        return self.car, self.vin


