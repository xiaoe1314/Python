# -*- coding: utf-8 -*-
import scrapy
import csv
from linkedin.items import LinkedinItem


# 1. 先从csv获取所有的公司（设置到请求谷歌的官网）
# 2. 从请求到的谷歌搜索网页中获取每条数据的领英url
# 3. 然后在登录领英，获取cookie, 在爬取个人中心的数据
# 4. 将获取到数据保存到content.csv文件中

# 定义领英url表头
urlHeaders = ['urls']
urlValues = []
urlValue = {}

companyValues = []
company = []

# 定义保存数据的表头
contentHeaders = ['企业', '姓名', '头像']

class LinkedinScrapySpider(scrapy.Spider):
    name = 'linkedin_scrapy'
    allowed_domains = ['google.com.hk']
    start_urls = ['https://www.google.com.hk//search?q=site:https://www.linkedin.com/in/*+%22engineer%22%22NTT%22&ei=L3jOW7PDA4zcwALjqq_QDQ&start=470&sa=N']
    base_url = 'https://www.google.com.hk/'

    def parse(self, response):
        urls = response.xpath("//div[@class='srg']/div[@class='g']//div[@class='r']//cite/text()").getall()
        # item = LinkedinItem(urls=urls)
        # yield item
        for url in urls:
            urlValue = {'urls': url}
            urlValues.append(urlValue)

        self.parse_urls(urlValues)

        next_url = response.xpath("//tr[@valign='top']/td[last()]/a/@href").get()
        if not next_url:
            for companyValue in self.parse_read_company():
                yield scrapy.Request(companyValue, callback=self.parse)
        else:
            yield scrapy.Request(self.base_url + next_url, callback=self.parse)

    def parse_read_company(self):
        # 通过字典读取文件
        with open('company.csv', 'r') as fp:
            # 使用DictReader创建的reader对象
            # 不会包含的那行数据
            reader = csv.DictReader(fp)
            for x in reader:
                value = {'WorldRank': x['WorldRank'], 'Company': x['Company']}

                url = 'https://www.google.com.hk/search?q=site:https://www.linkedin.com/in/* "engineer" "%s"' % value['Company']
                companyValues.append(url)

            return companyValues

    def parse_write_content(self):

        # 数据是字典形式
        values = [
            {'企业': 'VOLKSWAGEN', '姓名': 'zhang1',
             '头像': 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_86d58ae1.png'},
            {'企业': 'VOLKSWAGEN', '姓名': 'zhang2',
             '头像': 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_86d58ae1.png'},
            {'企业': 'VOLKSWAGEN', '姓名': 'zhang3',
             '头像': 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_86d58ae1.png'}
        ]
        # newline 是写入一行后做的事
        with open('content.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, contentHeaders)
            # 写入表头数据的时候，需要执行writeheader函数
            writer.writeheader()
            writer.writerows(values)


    def parse_urls(self, urlValues):
        # newline 是写入一行后做的事
        with open('urls.csv', 'w', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, urlHeaders)
            # 写入表头数据的时候，需要执行writeheader函数
            writer.writeheader()
            writer.writerows(urlValues)