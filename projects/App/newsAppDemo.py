import unittest
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import random


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.caps = {
            "platformName": "Android",
            "platformVersion": "4.4.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "topevery.zhcg.client",
            "appActivity": "topevery.um.client.mian.ClientLogin",
            # 输入法的安装与重置
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.caps)

    def test_user_logo(self):
        time.sleep(5)
        test = self.driver.page_source
        print(test)

    def tearDown(self):
        # 释放
        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
