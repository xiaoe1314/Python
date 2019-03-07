"""
    Created by 朝南而行 2019/2/27 9:31
"""

import re
import os
from urllib import request
from urllib import parse


def print_demo():
    print('123456', '123465')
    print('123456', end='\n')


def input_demo():
    temp = input('input()的返回值始终是字符串：')
    print(type(temp))


def split_demo():
    a = '123,456,789'.split(',', 3)
    print(a)


def find_or_rfind_demo():
    # a = 'this is money'
    # print(a.find('is'))
    # print(a.rfind('is'))
    # print('15121212c4512d12'.lstrip('12'))
    # a = '123Adfa'
    # print(a.ljust(len(a)+1, '}').rjust(len(a)+2, '{'))
    # print(abs(-123456))
    # print(complex(1, 2j))

    # http协议：超文本传输协议，是一直接收和发布HTML页面的方法，默认端口是80端口
    # https协议：是http协议的加密版本，在http下加了ssl层，也是安全层，服务端的端口是443端口
    # urllib是爬虫最基本的网络请求库，可以模拟浏览器行为

    # file_path = os.path.split(os.path.dirname(__file__))
    # print(type(file_path))
    # print(file_path)

    # qs = parse.urlencode(data)
    # qs = parse.parse_qs(qs)
    # print(type(qs))
    # print(''.join(qs['wd']))

    # a = [1,2,3,4,5,6]
    # result = ''
    # for x in a:
    #     result += str(x)
    # # print(''.join(a))
    # print(type(result))
    # print(a[10])
    # qs = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100"
    # print(parse.parse_qs(qs))

    # resp = request.urlopen('https://www.baidu.com')
    # print(resp.getcode())
    # file_path = os.path.split(__file__)
    # print(__file__)
    # print(file_path)
    # print(os.path.join(file_path))
    # request.urlretrieve('https://www.baidu.com', os.path.join(file_path, 'baidu.html'))
    # a = "{'a': 1, 'b': 10, 'c': 12}"
    # c = {1,2,3,4}
    # e = {1,2,3,4,5}
    #
    # # b = eval(a)
    # # c = tuple(c)
    # d = c.difference()
    # # print(b['a'])
    # print(d)
    # print(ord('1'))

    a = '时间在线校准，北京现在时间：2019-03-07 16:44:41。查世界各大城市时差'
    # r = re.compile(r'[\d]+-[\d]+-[\d]+\s[\d]+:[\d]+:[\d]+',re.VERBOSE)
    # r = re.compile(r'[\w\-\s:]+',re.VERBOSE)
    # ret = re.search(r, a)
    # print(ret.groups())
    # print(re.findall(r'时间：(.*?)。.*?', a, re.DOTALL))
    # print(re.findall(r'时间：([\w\-\s:]+)。.*?', a, re.DOTALL))

if __name__ == '__main__':
    find_or_rfind_demo()
