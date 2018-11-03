
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium 抓取Boss直聘职位信息


class LagouSpider(object):
    driver_path = r'E:\Python\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=python&scity=100010000'
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        while True:
            # page_source这个方法可以拿到全部代码包括ajax返回来的
            source = self.driver.page_source
            self.parse_list_page(source)
            # 等待
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page']//a[last()]"))
            )

            next_btn = self.driver.find_element_by_xpath("//div[@class='page']//a[last()]")

            # get_attribute获取属性
            if 'next disabled' in next_btn.get_attribute("class"):
                pass
            else:
                next_btn.click()

            time.sleep(2)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']//h3[@class='name']/a/@href")
        for link in links:
            self.request_detail_page('https://www.zhipin.com' + link)
            time.sleep(2)

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
        desc = re.sub(r"[\n]", "", "".join(html.xpath("//div[@class='detail-content']//div[@class='job-sec']//div[@class='text']//text()")).strip())

        position = {
            'company_name':company_name,
            'job_name':job_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }
        self.positions.append(position)
        print(position)
        print('='*200)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()











