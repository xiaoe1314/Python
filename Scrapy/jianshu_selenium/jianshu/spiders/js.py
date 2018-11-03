# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    # /p/7ba4ea51d56c?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
    # /p/7ba4ea51d56c
    # 两种url形式 .* 代表前面可有可无 [0-9a-z]{12} 0到9或者a到z的任意12位字符 后面的参数可有可无
    rules = (
        # Rule 是元组 后面必须要有英文状态下的逗号,
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath("//div[@class='article']/h1[@class='title']/text()").get().strip()
        avatar = response.xpath("//div[@class='article']/div[@class='author']/a/img/@src").get().strip()
        author = response.xpath("//div[@class='article']//div[@class='info']/span/a/text()").get().strip()
        pub_time = response.xpath("//div[@class='meta']/span[@class='publish-time']/text()").get().strip()
        origin_url = response.url
        # /p/7ba4ea51d56c?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
        # /p/7ba4ea51d56c
        # url里面只能有一个? 然后取第一个位 在通过/分割取最后一位
        author_id = response.url.split('?')[0].split('/')[-1]
        content = response.xpath("//div[@class='show-content-free']").get()
        read_count = response.xpath("//div[@class='meta']/span[@class='views-count']/text()").get().strip()
        like_count = response.xpath("//div[@class='meta']/span[@class='likes-count']/text()").get().strip()
        word_count = response.xpath("//div[@class='meta']/span[@class='wordage']/text()").get().strip()
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div[@class='name']/text()").getall()).strip()
        comment_count = response.xpath("//div[@class='meta']/span[@class='comments-count']/text()").get().strip()
        item = JianshuItem(
            title=title,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            origin_url=origin_url,
            author_id=author_id,
            content=content,
            read_count=read_count,
            like_count=like_count,
            word_count=word_count,
            subjects=subjects,
            comment_count=comment_count
        )
        yield item
