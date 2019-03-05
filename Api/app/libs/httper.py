"""
    Created by 朝南而行 2018/12/5 16:36
"""

import requests
from lxml import etree


# class HTTP 和 HTTP(object) python3无区别都是新式类
# python2 经典类和新式类
class HTTP:
    def __init__(self):
        # 1.将目标网站的页面抓取下来
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&srcqid=2328577874318033697&tn=93006350_hao_pg&wd=douban&oq=%25E8%2585%25BE%25E8%25AE%25AF%25E6%258B%259B%25E8%2581%2598&rsv_pq=a5c9fad500032d39&rsv_t=c45fuFhfw1QXFIl989itMrzlcssxBzOrrVGSndzUMM1KcQQn7C8JY6zoz3pfqLSKLuTd0%2FO8&rqlang=cn&rsv_enter=1&inputT=5137&rsv_sug3=33&rsv_sug2=0&rsv_sug4=5138'
        }

    def get(self, url, return_json=True):
        # 2.将抓取下来的数据根据一点的规则进行提取
        r = requests.get(url=url, headers=self.headers)
        if r.status_code != 200:
            parser = etree.HTMLParser(encoding='utf-8')
            html = etree.HTML(r, parser=parser)
            url = html.xpath('//li/@class')
            return {} if return_json else ''
        return r.json() if return_json else r.text


