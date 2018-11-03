# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
import time
import random
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Python\chromedriver.exe')

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(random.randint(1, 2))
        try:
            while True:
                showMore = self.driver.find_element_by_xpath("//a[@class='show-more']")
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass
        # 获取网页源代码
        source = self.driver.page_source
        # 在把源代码封装成response对象 current_url当前URL
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response























