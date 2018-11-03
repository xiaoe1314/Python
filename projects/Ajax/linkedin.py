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
        self.url = 'https://www.linkedin.com/uas/login'
        self.urlSearch = 'https://www.linkedin.com/feed/'
        self.urlKeys = ['key_one', 'key_two']
        self.positions = []
        self.urlValues = []

    def run(self):
        # 打开浏览器的一个网页
        self.driver.get(self.url)

        time.sleep(random.randint(1, 2))

        inputKey = self.driver.find_element_by_id('session_key-login')
        # 发送(输入)字符串
        inputKey.send_keys('18783164636')

        time.sleep(random.randint(1, 2))

        inputPassword = self.driver.find_element_by_id('session_password-login')
        # 发送(输入)字符串
        inputPassword.send_keys('zaq159159')

        time.sleep(random.randint(1, 2))

        submitTag = self.driver.find_element_by_id('btn-primary')
        # 执行点击事件
        submitTag.click()

        time.sleep(random.randint(3, 5))

        # 等待
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@role='combobox']"))
        )

        inputSearch = self.driver.find_element_by_xpath("//input[@role='combobox']")

        # 发送(输入)字符串
        inputSearch.send_keys('BMW')

        time.sleep(random.randint(1, 2))

        submitSearch = self.driver.find_element_by_xpath("//li-icon[@size='medium']")
        # 执行点击事件
        submitSearch.click()

        time.sleep(random.randint(1, 2))

        # 等待
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//button[@class='search-filters-bar__all-filters button-tertiary-medium-muted flex-shrink-zero mr3']"))
        )

        changeButton = self.driver.find_element_by_xpath(
            "//button[@class='search-filters-bar__all-filters button-tertiary-medium-muted flex-shrink-zero mr3']")

        # 执行点击事件
        changeButton.click()

        time.sleep(random.randint(3, 5))

        # 输入职位信息
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search-advanced-title']"))
        )

        inputTitle = self.driver.find_element_by_xpath("//input[@id='search-advanced-title']")
        # 发送(输入)字符串
        inputTitle.send_keys('engineer')

        time.sleep(random.randint(1, 2))

        # 点击确定按钮
        sureButton = self.driver.find_element_by_xpath(
            "//button[@class='search-advanced-facets__button--apply button-primary-large']")

        # 执行点击事件
        sureButton.click()

        time.sleep(random.randint(5, 10))

        while True:
            self.driver.execute_script("window.scrollTo(0, 800)")

            time.sleep(random.randint(3, 5))

            # page_source这个方法可以拿到全部代码包括ajax返回来的
            source = self.driver.page_source
            self.parse_list_page(source)

            # 等待
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='next']"))
            )

            # next_btn = self.driver.find_element_by_xpath("//span[@class='artdeco-button__text']")
            next_btn = self.driver.find_element_by_xpath("//button[@class='next']")

            next_btn.click()

            print('点击下一页')

            time.sleep(random.randint(6, 8))

    def parse_list_page(self, source):
        html = etree.HTML(source)

        # links = html.xpath("//ul[@class='search-results__list list-style-none mt2']//div[2]//span[@dir='ltr']/text()")
        links = html.xpath("//ul[@class='search-results__list list-style-none mt2']//li")
        categorys = html.xpath(
            "//ul[@class='search-results__list list-style-none mt2']//div[2]/p[1]//span[@dir='ltr']/text()")
        citys = html.xpath(
            "//ul[@class='search-results__list list-style-none mt2']//div[2]/p[2]//span[@dir='ltr']/text()")
        print(len(links))
        print(len(categorys))
        print(len(citys))

        for i, link in enumerate(links):
            urlValue = {
                'key_one': categorys[i],
                'key_two': citys[i],
            }
            print("categorys：" + categorys[i])
            print("city：" + citys[i])
            self.urlValues.append(urlValue)
            time.sleep(1)

        self.parse_urls(self.urlValues)

    def parse_urls(self, urlValues):
        # newline 是写入一行后做的事
        with open('keys.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, self.urlKeys)
            # 写入表头数据的时候，需要执行writeheader函数
            writer.writeheader()
            writer.writerows(urlValues)

    def request_detail_page(self, url):
        # 打开详情的窗口
        self.driver.execute_script("window.open('%s')" % url)
        # 切换到详情的窗口
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])

        source = self.driver.page_source
        self.parse_detail_page(source)

        # 关闭详情的窗口
        self.driver.close()
        # 切换到列表页
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        company_name = html.xpath("//h3[@class='name']/a/text()")[0]
        job_name = html.xpath("//div[@class='name']/h1/text()")[0]
        salary = html.xpath("//div[@class='name']//span[@class='badge']/text()")[1]
        # . 点号代表当前下面
        job_request_spans = html.xpath("//div[@class='info-primary']/p//text()")
        city = re.sub(r"城市：", "", job_request_spans[0].strip())
        work_years = re.sub(r"经验：", "", job_request_spans[1].strip())
        education = re.sub(r"学历：", "", job_request_spans[2].strip())
        # # "".join 将列表组合成字符串
        desc = re.sub(r"[\n]", "", "".join(
            html.xpath("//div[@class='detail-content']//div[@class='job-sec']//div[@class='text']//text()")).strip())

        position = {
            'company_name': company_name,
            'job_name': job_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.positions.append(position)
        print(position)
        print('=' * 200)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
