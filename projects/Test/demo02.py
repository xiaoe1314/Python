"""
    Created by 朝南而行 2019/2/27 9:31
"""


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

    print(complex(1, 2j))

if __name__ == '__main__':
    find_or_rfind_demo()
