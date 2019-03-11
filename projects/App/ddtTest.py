"""
    Created by 朝南而行 2019/3/11 17:09
"""

from ddt import ddt, data, unpack
import unittest


# 在需要测试的类加@ddt, 则这个类就添加了数据驱动
@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp')


    # 一个参数
    # @data(1, 2, 3)
    # def test_something(self, value1):
    #     print(str(value1))
    #     self.assertEqual(value1, 2)

    # 多参数
    @data(
        (1, 2),
        (2, 3),
        (3, 4)
    )
    @unpack
    def test_anything(self, value1, value2):
        print(str(value1) + "===" + str(value2))
        self.assertEqual(value1, value2)

    def tearDown(self):
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
