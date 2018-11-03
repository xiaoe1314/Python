
import requests
from lxml import etree
from urllib import request
import os
import re

# 实战-下载表情包之同步爬虫完成


def parse_page(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        # 获取图片的名字和获取图片的后缀才能拼接一个图片
        alts = img.get('alt')
        alt = re.sub(r'[\?？!！，,\.。、 （）\*]', '',alts)
        # os模块可以分割 . 后面的后缀
        suffixs = os.path.splitext(img_url)[1]
        suffix =re.sub('!dta','',suffixs)
        filename = alt + suffix
        # 保存图片下来，可以非常方便下载文件或者图片
        request.urlretrieve(img_url, 'images/'+filename)
        print(filename)


def main():
    for x in range(1, 2):
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)


if __name__ == '__main__':
    main()
