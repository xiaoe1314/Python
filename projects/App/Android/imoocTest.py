"""
    Created by 朝南而行 2019/4/9 19:52
"""


from appium import webdriver
import time
import unittest
from ddt import ddt, data, unpack
import warnings


@ddt
class ImoocTest(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        self.cap = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.android.browser',
            'appActivity': 'com.android.browser.BrowserActivity',
            # 'appWaitActivity': 'com.imooc.component.imoocmain.splash.MCSplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }

        # 获取屏幕的宽高
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.cap)


    @data(3)
    def test_run(self, num):
        # time.sleep(5)
        #
        # self.driver.find_element_by_id('tv_tips').click()
        # time.sleep(1)
        # self.driver.find_element_by_id('iv_close').click()
        # time.sleep(1)
        # self.driver.find_element_by_id('ll_item').click()
        time.sleep(20)
        webview = self.driver.contexts
        print(str(webview))


        # 点击某个位置
        # self.driver.tap([(self.splashLastPageX1, self.splashLastPageY1), (self.splashLastPageX2, self.splashLastPageY2)])

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
