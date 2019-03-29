"""
    Created by 朝南而行 2019/3/11 17:09
"""

from ddt import ddt, data, unpack
from projects.App import getCsvData
import unittest


# 在需要测试的类加@ddt, 则这个类就添加了数据驱动
@ddt
class MyTestCase(unittest.TestCase):

    list = getCsvData.read_csv()

    def setUp(self):
        print('setUp')

    # 一个参数
    # @data(*list)
    # def test_something(self, value1):
    #     print(str(value1))
    #     self.assertEqual(2, 2)

    # 多参数
    @data(*list)
    @unpack
    def test_anything(self, value1, value2):
        print(str(value1) + "===" + str(value2))
        self.assertEqual(2, 2)

    def tearDown(self):
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
