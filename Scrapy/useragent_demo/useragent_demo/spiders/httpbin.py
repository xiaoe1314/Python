# -*- coding: utf-8 -*-
import scrapy
import json


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        print(user_agent)
        # dont_filter=True设置不要去重（不要过滤）
        yield scrapy.Request(self.start_urls[0], dont_filter=True)

