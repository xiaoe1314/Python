
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


text = "hellHo"
# 匹配开头是h的字符
ret = re.match('^h.+', text)
# 匹配不是h的字符
ret_two = re.match('[^o]+?', text)
print(ret.group())
print(ret_two .group())
