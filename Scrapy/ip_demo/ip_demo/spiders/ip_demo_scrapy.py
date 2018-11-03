# -*- coding: utf-8 -*-
import scrapy
import json


class IpDemoScrapySpider(scrapy.Spider):
    name = 'ip_demo_scrapy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        print('*'*88)
        print(origin)
        print('*'*88)
        # dont_filter=True设置不要去重（不要过滤）
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
