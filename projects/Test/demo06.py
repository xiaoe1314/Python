"""
    Created by 朝南而行 2019/3/20 14:03
"""

# a = (1)
# b = (1)
# a = 1.0
# a = True
# a = 36j
# a = '123456'
# a = (1, 2, 3, 4)
# a = [1, 2, 3, 4]
# b = [8, 9, 2]
# a = {'11': '1', 'a': 123, 1: 3}
# print(id(a))
# print(id(b))


# for x in range(0, 100):
#     print(x)
# import re
# a = re.split(r'er', 'thissupermanri123')
# print(a)

# from sys import getrefcount
#
# a1 = 100000
# a2 = 100000
# # del a1
#
# print(getrefcount(a1))


a = {'key1': 1, 'key2': 2, 'key3': 3}

# for k, v in a.items():
#     print(k)
#     print(v)
print(a.get('key11', 'error'))
print(a['key1'])
