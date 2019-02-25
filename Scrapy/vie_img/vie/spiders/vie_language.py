# -*- coding: utf-8 -*-
import scrapy
from vie.items import VieItem


class VieLanguageSpider(scrapy.Spider):
    name = 'vie_language'
    allowed_domains = ['sound2.yywz123.com']
    start_urls = ['http://sound2.yywz123.com']

    def parse(self, response):
        # url = 'http://sound2.yywz123.com/vie/tingli/yngq/{}.mp3'
        
        # for x in range(600, 757):
        #     base_url = url.format(x)
        #     filename = base_url.split('/')[-1]
        #     yield VieItem(base_url=base_url, filename=filename)

        url = 'http://v.kd1.qq.com/shg_321_1116_22X0000000dz1HEhRVd3d5c1bc4a4739.f620.mp4' \
              '?dis_k=4f0cb86283d2b08cb728afd3dcff6c38&dis_t=1545790690'

        filename = url.split('?')[0].split('_')[-1].replace('.', '', 1)

        yield VieItem(base_url=url, filename=filename)
