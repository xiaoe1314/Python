"""
    Created by 朝南而行 2018/12/30 17:05
"""


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium 回复简书作者


class JianshuSpider(object):
    driver_path = r'E:\Python\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=JianshuSpider.driver_path)
        self.url = 'https://www.jianshu.com/c/f489ec955505'

    def run(self):
        self.login()


    def login(self):
        self.driver.get(self.url)
        print('正在等待登录中...')
        # 等待 登录
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='user']/div/a"))
        )
        print('登录成功')

        time.sleep(3)
        # # 等待
        # WebDriverWait(driver=self.driver, timeout=20).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//ul[@class='trigger-menu']/li[3]"))
        # )
        # # 执行热门文章选项
        # clickUser = self.driver.find_element_by_xpath(
        #     "//ul[@class='trigger-menu']/li[3]")
        # 等待
        # WebDriverWait(driver=self.driver, timeout=20).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//ul[@class='trigger-menu']/li[3]"))
        # )
        # # 执行热门文章选项
        # clickUser = self.driver.find_element_by_xpath(
        #     "//ul[@class='trigger-menu']/li[3]")
        # clickUser.click()
        # time.sleep(5)
        self.user_detail()

    def user_detail(self):
        i = 1
        y = 100
        while True:
            self.driver.execute_script("window.scrollTo(0, %d)" % y)
            y += 100
            # 等待
            WebDriverWait(driver=self.driver, timeout=20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='list-container']/ul/li[%d]/div[@class='content']/a" % i))
            )
            # 执行点击事件
            clickUser = self.driver.find_element_by_xpath(
                "//div[@id='list-container']/ul/li[%d]/div[@class='content']/a" % i)
            clickUser.click()
            time.sleep(2)
            # 切换到最后一个窗口
            self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2150)")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2100)")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2050)")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2000)")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1950)")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2050)")
            time.sleep(1)
            # for x in range(1, 5):
            #     gy = y * x
            #     js = "var q=document.getElementById('id').scrollTop=%d" % gy
            #     self.driver.execute_script(js)
                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-%d)" % y)
            # target = self.driver.find_element_by_xxxx()
            # self.driver.execute_script("arguments[0].scrollIntoView();", target)
            # # 查找文章回复框
            WebDriverWait(driver=self.driver, timeout=200).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='comment-list']//form[@class='new-comment']/textarea"))
            )
            # 发送(输入)字符串
            inputContent = self.driver.find_element_by_xpath(
                "//div[@id='comment-list']//form[@class='new-comment']/textarea")

            content = '''
            用了这个方法记单词，我词汇过万，
            8小时，累积解析英语词汇量1598（附资料）:
            https://www.jianshu.com/p/6db2c79fec43
            '''
            inputContent.send_keys(content)
            time.sleep(2)

            # 等待
            WebDriverWait(driver=self.driver, timeout=20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='comment-list']//form[@class='new-comment']/div/a[1]"))
            )
            inputContent = self.driver.find_element_by_xpath("//div[@id='comment-list']//form[@class='new-comment']/div/a[1]")
            # 发送(输入)字符串
            inputContent.click()
            print('回复成功')
            time.sleep(3)
            i += 1
            # 关闭最后一个窗口
            self.driver.close()
            time.sleep(2)
            self.driver.switch_to_window(self.driver.window_handles[0])


        # # 打开高校的窗口
        # self.driver.execute_script("window.open('%s')" % self.school_url)
        # # 切换到首页的窗口
        # self.driver.switch_to_window(self.driver.window_handles[0])
        # # 关闭首页的窗口
        # self.driver.close()
        # # 切换到高校的窗口
        # self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        # time.sleep(2)
        # print('开始进入所有高校页===' + self.school_url)

        # while True:
        #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(3)
        #     # page_source这个方法可以拿到全部代码包括ajax返回来的
        #     source = self.driver.page_source
        #     self.parse_list_page(source)
        #     # 等待
        #     WebDriverWait(driver=self.driver, timeout=10).until(
        #         EC.presence_of_element_located((By.XPATH, "//div[@class='pagination']//a[@class='next']"))
        #     )
        #     next_btn = self.driver.find_element_by_xpath("//div[@class='pagination']//a[@class='next']")
        #     # get_attribute获取属性
        #     if 'next' in next_btn.get_attribute("class"):
        #         next_btn.click()
        #     else:
        #         pass
        #     time.sleep(2)


if __name__ == '__main__':
    spider = JianshuSpider()
    spider.run()











