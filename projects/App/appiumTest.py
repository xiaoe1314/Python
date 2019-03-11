"""
    Created by 朝南而行 2019/3/8 17:21
"""

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random


class AppiumQTT(object):

    def __init__(self):
        self.cap = {
            "platformName": "Android",
            "platformVersion": "4.4.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.jifen.qukan",
            "appActivity": "com.jifen.qkbase.main.MainActivity",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.cap)
        time.sleep(5)
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
        self.x1 = int(self.x * 0.5)
        self.y1 = int(self.y * 0.75)
        self.y2 = int(self.y * 0.25)

    def swipe_in(self):
        a = 5
        while a > 0:
            print('开始向上滑动=================================' + str(5-a))
            self.driver.swipe(self.x1, self.y1, self.x1, self.y2)
            time.sleep(random.randint(8, 12))
            a = a - 1

    def swipe_up(self):
        b = 3
        while b > 0:
            print('开始向下滑动=================================' + str(5 - b))
            self.driver.swipe(self.x1, self.y2, self.x1, self.y1)
            time.sleep(random.randint(8, 12))
            b = b - 1

    def swipe_random(self):
        c = random.randint(2, 5)
        while c > 0:
            print('随机滑动=================================' + str(c))
            self.driver.swipe(self.x1, self.y1, self.x1, self.y2)
            time.sleep(random.randint(1, 2))
            c = c - 1

    def run(self):
        while True:
            print('开始点击列表=================================')
            try:
                if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.jifen.qukan:id/pr']/android.widget.LinearLayout[1]")):
                    self.driver.find_element_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.jifen.qukan:id/pr']/android.widget.LinearLayout[1]").click()
            except Exception as e:
                print(e)
                pass
            self.swipe_in()
            self.swipe_up()
            # 点击返回键
            self.driver.keyevent(4)
            time.sleep(3)
            self.swipe_random()


if __name__ == '__main__':
    appiumQtt = AppiumQTT()
    appiumQtt.run()

