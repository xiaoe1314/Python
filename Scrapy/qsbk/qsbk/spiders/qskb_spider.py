# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from qsbk.items import QsbkItem

class QskbSpiderSpider(scrapy.Spider):
    name = 'qskb_spider'
    allowed_domains = ['qiushibaike.com']
    # 要提前下一页的链接在爬取
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = 'https://www.qiushibaike.com'

    def parse(self, response):
        print('=' * 50)
        # SelectorList
        divs = response.xpath("//div[@id='content-left']/div")
        # items = []
        for div in divs:
            # Selector
            author = div.xpath(".//h2/text()").get().strip()
            content = "".join(div.xpath(".//div[@class='content']//span/text()").getall()).strip()
            # 获取得数据之后移交给Pipeline存储(yield duanzi)
            item = QsbkItem(author=author, content=content)
            # yield 之后返回当前item
            yield item
            # items.append(item)
        # return items

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_url+next_url, callback=self.parse)
