# -*- coding: utf-8 -*-
import scrapy


# 使用post方式请求
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # 1.必须重写start_requests
    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            "email": '15907813604',
            "password": 'zzll04052313'
        }
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    # 登录成功后会保存cookie信息，可以访问需要登录的页面
    def parse_page(self, response):
        # 访问需要登录才能访问的主页
        request = scrapy.Request('http://www.renren.com/857190731/profile?portal=homeFootprint&ref=home_footprint', callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('other.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
















