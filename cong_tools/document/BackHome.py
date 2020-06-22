# coding=utf-8
__author__ = 'cong'


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import os


class BackHome(object):
    def __init__(self, url):
        ipath = os.path.dirname(os.path.dirname(__file__)) + '/Driver/geckodriver.exe'
        os.environ["webdriver.firefox.driver"] = ipath
        self.driver = webdriver.Firefox(executable_path=ipath, service_log_path=None)
        self.driver.get(url)

    def name(self, args):
        # 输入出名字
        # Name = '聪'
        self.driver.implicitly_wait(10)
        name = self.driver.find_element_by_css_selector('div.kuma-input-uxform-field:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        # for i in args:
        # time.sleep(random.random())
        #     name.send_keys(i)
        name.send_keys(args)

    def job_number(self, args):
        self.driver.implicitly_wait(10)
        # 输入工号
        # Name_word = 'wb-zc193433'
        # time.sleep(2)
        name_word = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(2) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        # for j in args:
        #     time.sleep(random.random())
        #     name_word.send_keys(j)
        name_word.send_keys(args)

    def date(self):
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        # 选择日期
        da = self.driver.find_element_by_css_selector('.kuma-calendar-picker-input')
        ActionChains(self.driver).click(da).perform()
        # 设置等待时间
        self.driver.implicitly_wait(10)
        dt = self.driver.find_element_by_xpath('//*[@class="kuma-calendar-date"][@aria-selected="true"]')
        ActionChains(self.driver).click(dt).perform()

    def company(self, args):
        self.driver.implicitly_wait(10)
        # time.sleep(2)
        # 外包公司
        wb = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(4) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        # 鼠标点击
        ActionChains(self.driver).click(wb).perform()
        wb1 = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(4) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > \
        input:nth-child(1)')
        # 键盘输入
        # wb1.send_keys('诚迈')
        # for i in args:
        #     time.sleep(random.random())
        #     wb1.send_keys(i)
        wb1.send_keys(args)
        self.driver.implicitly_wait(10)
        # 键盘ENTER
        # time.sleep(1)
        wb1.send_keys(Keys.ENTER)

    def project(self, args):
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        # 项目
        xm = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(5) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        ActionChains(self.driver).click(xm).perform()
        xm1 = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(5) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > \
        input:nth-child(1)')
        # for i in args:
        #     time.sleep(random.random())
        #     xm1.send_keys(i)
        xm1.send_keys(args)
        # time.sleep(1)
        self.driver.implicitly_wait(10)
        xm1.send_keys(Keys.ENTER)

    def task(self, args):
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        # 任务
        lw = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(6) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        ActionChains(self.driver).click(lw).perform()
        lw1 = self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(6) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > \
        input:nth-child(1)')
        # for i in args:
        #     time.sleep(random.random())
        #     lw1.send_keys(i)
        # time.sleep(1)
        lw1.send_keys(args)
        self.driver.implicitly_wait(10)
        lw1.send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector('div.kuma-uxform-field:nth-child(7) > div:nth-child(1) > ul:nth-child(2) > \
        li:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(9)

    def quit(self):
        time.sleep(30)
        self.driver.quit()


if __name__ == '__main__':
    name = '周聪'
    job_name = 'wb-zc193433'
    company = '诚迈'
    project = '福特'
    task = '测试用例及测试报告'
    url = 'https://www.aliwork.com/alibaba/web/APP_SEV4BNNJ6PPK40RBN3UN/inst/formSubmit.html?\
            formUuid=FORM-ZIYJ8JEVWTY4XCPCY2LF8SQ4IO1W1NS2WQXUJ7#/'
    try:
        home = BackHome(url)
        home.name(name)
        home.job_number(job_name)
        home.date()
        home.company(company)
        home.project(project)
        home.task(task)
        home.quit()
    except:
        pass
