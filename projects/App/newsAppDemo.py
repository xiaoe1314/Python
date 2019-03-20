import unittest
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import random


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.caps = {
            "platformName": "Android",
            # "platformVersion": "4.4.2",
            # "deviceName": "127.0.0.1:62001",
            "platformVersion": "6.0.1",
            "deviceName": "818c3590",
            "appPackage": "com.yanhui.qktx",
            "appActivity": "com.yanhui.qktx.activity.SplashActivity",
            # 输入法的安装与重置
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.caps)

    def test_user_logo(self):
        time.sleep(10)
        test = self.driver.page_source
        print(test)
        # time.sleep(10)
        img_close = self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.yanhui.qktx:id/img_close']")
        img_close.click()
        time.sleep(10)
        # print('img_close点击成功')
        # time.sleep(5)
        #
        # first_view = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.yanhui.qktx:id/main_bottom_user']/android.widget.LinearLayout[1]")
        # first_view.click()
        # print('first_view点击成功')
        # time.sleep(2)
        #
        # img_user_logo = self.driver.find_element_by_id('img_user_logo')
        # img_user_logo.click()
        # print('img_user_logo点击成功')
        # time.sleep(2)
        #
        # user_info_photo = self.driver.find_element_by_id('activity_user_info_photo_rela')
        # user_info_photo.click()
        # print('user_info_photo点击成功')
        # time.sleep(2)
        #
        # btn_take_photo = self.driver.find_element_by_id('btn_take_photo')
        # btn_take_photo.click()
        # print('btn_take_photo点击成功')
        # time.sleep(2)
        #
        # try:
        #     if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('button1')):
        #         button1 = self.driver.find_element_by_id('button1')
        #         button1.click()
        #         time.sleep(2)
        # except Exception as e:
        #     print(e)
        #     pass
        #
        # try:
        #     if WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id('v6_shutter_button_internal')):
        #         shutter_button = self.driver.find_element_by_id('v6_shutter_button_internal')
        #         shutter_button.click()
        #         time.sleep(2)
        # except Exception as e:
        #     print(e)
        #     pass
        #
        # try:
        #     if WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id('v6_btn_done')):
        #         v6_btn_done = self.driver.find_element_by_id('v6_btn_done')
        #         v6_btn_done.click()
        #         time.sleep(2)
        # except Exception as e:
        #     print(e)
        #     pass
        #
        # try:
        #     if WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id('btn_ok')):
        #         btn_ok = self.driver.find_element_by_id('btn_ok')
        #         btn_ok.click()
        #         time.sleep(3)
        # except Exception as e:
        #     print(e)
        #     pass
        #
        # user_name = self.driver.find_element_by_id('activity_userinfo_et_name')
        # user_name.click()
        # time.sleep(2)
        # et_input_name = self.driver.find_element_by_id('et_input_name')
        # et_input_name.clear()
        # time.sleep(1)
        # et_input_name.send_keys(random.randint(1, 5))
        # time.sleep(1)
        # dialog_input_name = self.driver.find_element_by_id('view_dialog_in_put_name_commint')
        # dialog_input_name.click()
        # time.sleep(2)
        # print('user_logo')
        self.assertEqual(True, True)

    def tearDown(self):
        # 释放
        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
