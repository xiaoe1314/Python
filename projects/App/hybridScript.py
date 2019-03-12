import unittest
from appium import webdriver
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.caps = {
            "platformName": "Android",
            "platformVersion": "4.4.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.ijinshan.browser_fast",
            "appActivity": "com.ijinshan.browser.screen.BrowserActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "automationName": "Selendroid",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.caps)
        time.sleep(5)

    def test_something(self):
        print('test_something')
        baidu = self.driver.find_element_by_xpath("//android.widget.TextView[@text='百度']")
        baidu.click()
        time.sleep(3)
        baidu_top = self.driver.find_element_by_id('address_bar_hint')
        baidu_top.click()
        time.sleep(1)
        baidu_address = self.driver.find_element_by_id('address_bar_edit_text')
        baidu_address.send_keys('http://wap.sogou.com')
        baidu_address_go = self.driver.find_element_by_id('address_confirm_button')
        baidu_address_go.click()
        time.sleep(5)

        # switch_to 切换当前上下文
        print('switch_to 切换当前上下文===' + self.driver.contexts)
        self.driver._switch_to.context('')
        self.assertEqual(True, True)

    def tearDown(self):
        print('tearDown')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
