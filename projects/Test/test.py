
import re
# import json
#
# a = 5
# getMyself = []
# info = {}
# infoDetail = {}
# info['code'] = 200
# info['msg'] = '请求成功'
# info['data'] = getMyself
# while a > 0:
#     print('a===' + str(a))
#     infoDetail['name'] = '小明'
#     infoDetail['age'] = str(a)
#     getMyself.append(infoDetail)
#     a = a - 1
#
# print(json.dumps(info, ensure_ascii=False))

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10000:
#     print(b, end=',')
#     a, b = b, a+b

# 输入狗的年龄，然后输入狗的特征
# age = int(input('请输入狗狗的年龄:'))
# human = 22 + (age - 2)*5
# if age < 0:
#     print("Are you kidding  me")
# elif age == 1:
#     print('相当于12岁年龄的孩子')
# elif age == 2:
#     print('相当于22岁的成年人的智商了')
# else:
#     print('相当于人类年龄：' + str(human))
# input('按enter键退出')


# sites = ["Baidu", "Google","Runoob","Taobao"]
# # sites = {'a':1, 'b':"666"}
# # for site in sites:
# #     print(sites[site])
# for site in range(len(sites)):
#     print(sites[site])
#     if sites[site] == 'Baidu':
#         continue
#     print(site)

# import calendar
#
# cal = calendar.month(2018, 10)
# print("以下输出2018年2月份的日历:")
# print(cal)

# class MyNumbers:
#     def __iter__(self):
#         while self:


# a = 'boofdasbvoobbyd123'
#
# a_test = re.match(".*?(b.*?b).*", a)
# print(a_test.group())


# text = "hellHo"
# # 匹配开头是h的字符
# ret = re.match('^h.+', text)
# # 匹配不是h的字符
# ret_two = re.match('[^o]+?', text)
# print(ret.group())
# print(ret_two .group())
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import os, requests
from contextlib import closing

a = 'http://b317.photo.store.qq.com/psbe?/V12d1wl910x6ss/VIys*DZ7YV4MWjCOWdE.17Nf7ahi0NSIj6AdwgjiSFweozU62pIYuHAweCIZK4IJ/b/dD0BAAAAAAAA&bo=VAY4BHAXoA8RCZg!&rf=viewer_4'

# b = a.split('&')[-1]
#
# print(b)

path = os.path.join(os.path.dirname(__file__), 'img')
if not os.path.exists(path):
    os.mkdir(path)
    print('路径不存在')
else:
    print('路径存在')

with closing(requests.get(a, stream=True)) as response:
    chunk_size = 1024  # 单次请求最大值
    content_size = int(response.headers['content-length'])  # 内容体总大小
    data_count = 0
    with open(os.path.join(path, '1.jpg'), "wb") as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            data_count = data_count + len(data)
            now_jd = (data_count / content_size) * 100
            print("\r 文件下载进度：%d%%(%d/%d) - %s" %
                  (now_jd, data_count, content_size, a), end=" ")