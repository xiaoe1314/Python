import math
import random


# name = 'Runoob'
# print(r'Ru\noob')
# print(name[0:6])
# print(name[:])
# # input("\n\n按下 enter 键后退出。")
# # a, b, c = 1, 2, "runoob"
# counter = 100 # 整型变量
# miles = 1000.0 # 浮点型变量
# name = "runoob" # 字符串
# print(type(counter))
# print(type(miles))
# print(type(name))
# intMiles = int(miles)
# print(type(intMiles))
# print(isinstance(miles, int))
# print(10/4)
# print(10//4)
#
# del counter

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
# print (list) # 输出完整列表
# print (list[0]) # 输出列表第一个元素
# print (list[1:3]) # 从第二个开始输出到第三个元素
# print (list[2:]) # 输出从第三个元素开始的所有元素
# print (tinylist * 2) # 输出两次列表
# print (list + tinylist) # 连接列表
#
#
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
# print (dict['one']) # 输出键为 'one' 的值
# print (dict[2]) # 输出键为 2 的值
# print (dict) # 输出完整的字典
# print (tinydict.keys()) # 输出所有键
# print (tinydict.values()) # 输出所有值

#
# a = 10
# b = 10.0
#
# if not (a==b):
#     print("5")
# else:
#     print('6')
#
# if a is b :
#     print('6')
# a = 10
#
# print(random.Random(a))

# print("我叫 %s 今年 %d 岁!" % ('小明', 10))

# from urllib import request
# import chardet
# html = request.urlopen('http://www.runoob.com/python3/python3-string.html').read()
# print(chardet.detect(html))

import threading
from urllib import request
import time

class start_threading(threading.Thread):
    def run(self):
        for x in range(3):
            print("我正在下载%s次" % threading.current_thread())
            time.sleep(1)

class start_threading2(threading.Thread):
    def run(self):
        for x in range(3):
            print("2我正在下载%s次" % threading.current_thread())
            time.sleep(1)

if __name__ == '__main__':
    t1 = start_threading()
    t2 = start_threading2()

    t1.start()
    t2.start()
