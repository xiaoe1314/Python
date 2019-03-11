from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_something(self):
        print('test_something')
        # 断言
        self.assertEqual(True, True)

    def test_anything(self):
        print('test_anything')
        # 断言
        self.assertEqual(True, True)


    def tearDown(self):
        print('teardown')


if __name__ == '__main__':
    unittest.main()
