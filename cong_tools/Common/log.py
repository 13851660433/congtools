# coding=utf-8
__author__ = 'cong'


import logging
import time
import os


class mylog(object):
    def __init__(self, logger_name, path):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        rq = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        all_log_path = os.path.join(path, 'logs\\')
        # error_log_path = os.path.join(path, 'logs\\')
        all_log_name = all_log_path + rq + '.log'
        # error_log_name = error_log_path + rq + '.log'

        # 创建一个handler写入错误日志
        fh = logging.FileHandler(all_log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)
        eh = logging.FileHandler(all_log_name, encoding='utf-8')
        eh.setLevel(logging.ERROR)

        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    c = mylog('text').getlog()
    c.info('I am info')
    c.error('I am info')
