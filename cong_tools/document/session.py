# coding=utf-8
__author__ = 'cong'

import requests
import json


class TranSlate(object):
    def __init__(self, f):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            "kw": f
        }

        header = {
            'accept - language': 'zh - CN, zh;q = 0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user - agent': 'Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML, like Gecko)\
             Chrome/74.0.3729.157 Safari/537.36'
        }

        res = requests.post(url, data=data, headers=header)
        js = json.loads(res.text)
        for i in js['data']:
            print(i['k'], '-----', i['v'])
