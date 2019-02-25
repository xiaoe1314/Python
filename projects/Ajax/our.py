"""
    Created by 朝南而行 2018/12/30 17:05
"""


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import os, requests
from contextlib import closing

# selenium 回复简书作者


class JianshuSpider(object):
    driver_path = r'E:\Python\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=JianshuSpider.driver_path)
        self.url = 'https://user.qzone.qq.com/1035583363?source=aiostar'

        self.path = os.path.join(os.path.dirname(__file__), 'img')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            print('路径不存在')
        else:
            print('路径存在')

    def run(self):
        self.login()


    def login(self):
        self.driver.get(self.url)
        print('正在等待登录中...')
        # 等待 登录
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='QZ_Toolbar_Container']/div/div[1]/a[1]/span"))
        )
        print('登录成功')

        time.sleep(3)

        # 等待
        WebDriverWait(driver=self.driver, timeout=20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='js-image-ctn']"))
        )
        print('查找大图位置成功')
        time.sleep(2)
        self.user_detail()

    def user_detail(self):
        a = 1
        while True:
            # page_source这个方法可以拿到全部代码包括ajax返回来的
            source = self.driver.page_source
            html = etree.HTML(source)
            url = html.xpath("//div[@id='js-image-ctn']/img[1]/@src")
            print(url)
            if url:
                filename = a

                with closing(requests.get(url, stream=True)) as response:
                    chunk_size = 1024  # 单次请求最大值
                    content_size = int(response.headers['content-length'])  # 内容体总大小
                    data_count = 0
                    with open(os.path.join(self.path, filename), "wb") as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                            data_count = data_count + len(data)
                            now_jd = (data_count / content_size) * 100
                            print("\r 文件下载进度：%d%%(%d/%d) - %s" %
                                  (now_jd, data_count, content_size, url), end=" ")

            # # 等待
            WebDriverWait(driver=self.driver, timeout=20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[@id='js-btn-nextPhoto']"))
            )
            # 执行热门文章选项
            clickUser = self.driver.find_element_by_xpath(
                "//a[@id='js-btn-nextPhoto']")
            clickUser.click()
            time.sleep(3)

            a = a+1


if __name__ == '__main__':
    spider = JianshuSpider()
    spider.run()











