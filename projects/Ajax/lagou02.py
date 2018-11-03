
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium 抓取拉钩网职位信息


class LagouSpider(object):
    driver_path = r'E:\Python\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    def run(self):
        while True:
            self.driver.get(self.url)
            # page_source这个方法可以拿到全部代码包括ajax返回来的
            source = self.driver.page_source
            self.parse_list_page(source)
            # 打开新窗口
            self.driver.execute_script("window.open('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')")
            # switch_to_window切换窗口
            # print(len(self.driver.window_handles))
            self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles)-1])
            # 等待
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']//span[last()]"))
            )
            try:
                next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']//span[last()]")
                # get_attribute获取属性
                if 'pager_next pager_next_disabled' in next_btn.get_attribute("class"):
                    pass
                else:
                    next_btn.click()
            except:
                print(source)

            time.sleep(1)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(2)

    def request_detail_page(self, url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        # . 点号代表当前下面
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r"[\s/]", "", city)
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r"[\s/]", "", education)
        # "".join 将列表组合成字符串
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        position = {
            'name':position_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }
        self.positions.append(position)
        print(self.positions)
        print('='*200)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()











