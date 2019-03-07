"""
    Created by 朝南而行 2019/3/7 13:56
"""


import requests
import os
import re
from lxml import etree
import xlwt
import pymysql
import pandas as pd
import json
# from om dingtalkchatbot.chatbot imp import DingtalkChatbot
import time
import random
import pprint
# from selenium


headers = {
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '92',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_cfe2a1fc66d26c96eb2192ef8d25c599=1551680109,1551854257,1551854263,1551922416; Hm_lpvt_cfe2a1fc66d26c96eb2192ef8d25c599=1551927786; Hm_lvt_1479d5ddeb6580d8ae555defc49a3236=1551749764,1551832848,1551868572,1551920550; Hm_lpvt_1479d5ddeb6580d8ae555defc49a3236=1551923018',
    # 'Origin': 'http://jzsgl.coc.gov.cn',
    'Host': 'jzsgl.coc.gov.cn',
    'Referer': 'http://jzsgl.coc.gov.cn/archisearch/cxejjzs/qylist.aspx?sjbm=110000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.119 Safari/537.36',
    # 'X-Referer': 'http: // jzsgl.coc.gov.cn / archisearch / cxejjzs / qylist.aspx?sjbm = 110000',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    "action": '020102',
    'param': '{"Sjbm":"110000","Qymc":"","PageNo":1}'
}

web_url = "http://jzsgl.coc.gov.cn/archisearch/AjaxAction/DataServices.ashx"
response = requests.post(url=web_url, data=data, headers=headers)
text = response.content.decode("utf-8", errors="ignore")
print(text)
