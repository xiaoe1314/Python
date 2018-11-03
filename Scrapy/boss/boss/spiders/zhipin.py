# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


# 优化，加随机请求头和随机代理

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    # ? 是特殊字符，前面加反斜杠转义 \  .+ 最少有一个
    rules = (
        # 匹配列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        # 匹配职位详情的规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+.html?'), callback='parse_job', follow=False),
    )

    def parse_job(self, response):
        title = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='name']/span[@class='badge']/text()").get().strip()
        job_info = response.xpath("//div[@class='job-primary detail-box']//div[@class='info-primary']/p/text()").getall()
        city = job_info[0].strip()
        work_years = job_info[1].strip()
        education = job_info[2].strip()
        company = response.xpath("//div[@class='info-company']/h3[@class='name']/a/text()").get().strip()
        item = BossItem(title=title, salary=salary, city=city, work_years=work_years, education=education, company=company)
        # yield 给pipelines
        yield item
