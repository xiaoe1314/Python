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
            "appPackage": "com.yanhui.qktx",
            "appActivity": "com.yanhui.qktx.activity.SplashActivity",
            # 输入法的安装与重置
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # "automationName": "Selendroid",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.caps)
        time.sleep(5)

    def test_something(self):
        print('test_something')
        img_close = self.driver.find_element_by_id("img_close")
        img_close.click()
        time.sleep(3)
        first_view = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.yanhui.qktx:id/rv_news']/android.view.View[1]")
        first_view.click()
        time.sleep(3)

        # baidu_top = self.driver.find_element_by_id('address_bar_hint')
        # baidu_top.click()
        # time.sleep(1)
        # baidu_address = self.driver.find_element_by_id('address_bar_edit_text')
        # baidu_address.send_keys('http://wap.sogou.com')
        # baidu_address_go = self.driver.find_element_by_id('address_confirm_button')
        # baidu_address_go.click()
        # time.sleep(5)

        # switch_to 切换当前上下文
        # print('switch_to 切换当前上下文===' + str(self.driver.current_context))
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.get_clipboard_text()
        view_share = self.driver.find_element_by_id('view_share')
        view_share.click()
        time.sleep(3)
        view_share_url = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.yanhui.qktx:id/recycler_view']/android.widget.RelativeLayout[6]")
        view_share_url.click()
        time.sleep(3)
        self.assertEqual(True, True)

    def tearDown(self):
        print('tearDown')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
