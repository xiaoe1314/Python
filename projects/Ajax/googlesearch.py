from selenium import webdriver
from lxml import etree
import csv
import re
import time
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# selenium 抓取LinkedIn领英的公司员工信息


class LagouSpider(object):
    driver_path = r'E:\Python\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.google.com.hk/'
        self.urlSearch = 'https://www.linkedin.com/feed/'
        self.urlKeys = ['key_one', 'key_two']
        self.urls = ['urls']
        self.positions = []
        self.urlValues = []
        self.urlLinkedin = []

    def run(self):
        # 打开浏览器的一个网页
        self.driver.get(self.url)

        time.sleep(random.randint(3, 5))

        self.parse_read_company()

    def parse_read_company(self):
        # 通过字典读取文件
        with open('keys.csv', 'r') as fp:
            # 使用DictReader创建的reader对象
            # 不会包含的那行数据
            reader = csv.DictReader(fp)
            for x in reader:
                value = {'key_one': x['key_one'], 'key_two': x['key_two']}
                print(value)
                url = 'https://www.google.com.hk/search?q=site:https://www.linkedin.com/in/* "%s" "%s" "BMW"' % (x['key_one'], x['key_two'])
                print("url:" + url)
                self.request_detail_page(url)
                time.sleep(random.randint(10, 15))

    def request_detail_page(self, url):
        # 打开谷歌搜索的窗口
        self.driver.execute_script("window.open('%s')" % url)
        # 切换到谷歌搜索的窗口
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        time.sleep(random.randint(5, 6))
        source = self.driver.page_source
        self.parse_detail_google_page(source)

        # 关闭谷歌搜索的窗口
        self.driver.close()
        # 切换到首页
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_google_page(self, source):
        html = etree.HTML(source)
        urls = html.xpath("//div[@class='srg']/div[@class='g']//div[@class='r']/a[1]/@href")
        for url in urls:
            urlDetail = {"urls": url}
            self.urlLinkedin.append(urlDetail)

        self.parse_urls(self.urlLinkedin)

    def parse_urls(self, urlLinkedin):
        # newline 是写入一行后做的事
        with open('urls.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, self.urls)
            # 写入表头数据的时候，需要执行writeheader函数
            writer.writeheader()
            writer.writerows(urlLinkedin)


    # def parse_detail_page(self, source):
    #     html = etree.HTML(source)
    #     urls = html.xpath("//div[@class='srg']/div[@class='g']//div[@class='r']//cite/text()").getall()
    #     for url in urls:
    #
    #
    #     job_name = html.xpath("//div[@class='name']/h1/text()")[0]
    #     salary = html.xpath("//div[@class='name']//span[@class='badge']/text()")[1]
    #     # . 点号代表当前下面
    #     job_request_spans = html.xpath("//div[@class='info-primary']/p//text()")
    #     city = re.sub(r"城市：", "", job_request_spans[0].strip())
    #     work_years = re.sub(r"经验：", "", job_request_spans[1].strip())
    #     education = re.sub(r"学历：", "", job_request_spans[2].strip())
    #     # # "".join 将列表组合成字符串
    #     desc = re.sub(r"[\n]", "", "".join(
    #         html.xpath("//div[@class='detail-content']//div[@class='job-sec']//div[@class='text']//text()")).strip())
    #
    #     position = {
    #         'company_name': company_name,
    #         'job_name': job_name,
    #         'salary': salary,
    #         'city': city,
    #         'work_years': work_years,
    #         'education': education,
    #         'desc': desc
    #     }
    #     self.positions.append(position)
    #     print(position)
    #     print('=' * 200)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
