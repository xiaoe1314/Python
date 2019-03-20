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

    # a = '时间在线校准，北京现在时间：2019-03-07 16:44:41。查世界各大城市时差'
    # r = re.compile(r'[\d]+-[\d]+-[\d]+\s[\d]+:[\d]+:[\d]+',re.VERBOSE)
    # r = re.compile(r'[\w\-\s:]+',re.VERBOSE)
    # ret = re.search(r, a)
    # print(ret.groups())
    # print(re.findall(r'时间：(.*?)。.*?', a, re.DOTALL))
    # print(re.findall(r'时间：([\w\-\s:]+)。.*?', a, re.DOTALL))

    a = (5, 6, 7, 1, 9)
    b = [5, 6, 7, 1, 9]
    c = {5, 10, 17, 1, 9}
    #

    print(help(sorted))
    print(type(sorted(a)))
    print(sorted(a))
    print(sorted(c, reverse=True))


def sortedList(lists, reverse=False):
    count = len(lists) - 1
    for index in range(count, 0, -1):
        for index_sub in range(index):
            # 倒序
            if reverse:
                if lists[index_sub] < lists[index_sub + 1]:
                    lists[index_sub], lists[index_sub + 1] = lists[index_sub + 1], lists[index_sub]
            # 排序
            else:
                if lists[index_sub] > lists[index_sub+1]:
                    lists[index_sub], lists[index_sub+1] = lists[index_sub+1], lists[index_sub]

    return print(lists)


# def lambdaDemo():
    # a = {5, 6, 7, 1, 9}
    # l = [('a', 1), ('f', 2), ('c', 6), ('d', 4), ('e', 3)]
    # a = sorted(l, key=lambda x: x[0])
    # print(a)
    # print(type((1,2)))
    # print(l.sort(key=lambda x: x[0]))

# 质数（prime number）又称素数，有无限个。
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(0, 1000):
        if is_prime(i):
            print(i, end='=====')
