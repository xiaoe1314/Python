"""
    Created by 朝南而行 2019/3/6 11:24
"""

from lxml import etree
import requests
from bs4 import BeautifulSoup
import re


# lxml+xpath+requests
# BeautifulSoup4+requests
# 1.将目标网站的页面抓取下来
headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'https://movie.douban.com/explore'
}

url = 'https://movie.douban.com/'

resp = requests.get(url=url, headers=headers)
# text = resp.text
# parses = etree.HTMLParser(encoding='utf-8')
text = resp.content.decode('utf-8')
# print(text)
# html = etree.HTML(text)
# titles = html.xpath("//div[contains(@id, 'screening')]//ul")
# for title in titles:
#     url = title.xpath(".//li[@class='poster']/a/@href")[0]
#     print(url)
# soup = BeautifulSoup(text, 'lxml')
# titles = soup.select("div#screening > div.screening-bd > ul")
# for title in titles:
#     urls = title.select("li > a:noth")
#     for url in urls:
#         print(url.get('href'))
# for title in titles:
#     url = title.select("li .poster > a[href]")[0]
#     print(url)
# print(text)
# titles = re.findall(r'<li\sclass="poster">.*?<a.*?href="(.*?)".*?>.*?</a>', text, re.DOTALL)
# print(titles)
# for title in titles:
#     print(title)
# a = 257
# b = a

# if a == b:
#     print('true')
#     print('a 的')
# else:
#     print('false')
# print(id(a))
# print(id(b))
# print(a is b)
