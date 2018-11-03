import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

# 实战-下载表情包之多线程异步爬虫完成
# 1.获取每一页的url main()函数完成
# 2.生产者（获取每一页的图片url）
# 3.每个表情的url
# 4.消费者（下载图片）


#把队列传进来，需要重写init函数
class Procuder(threading.Thread):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    # 构造函数
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # 重写init函数 需要调用父类的init函数
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url=url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_urls = img.get('data-original')
            img_url = re.sub('!dta', '', img_urls)
            # 获取图片的名字和获取图片的后缀才能拼接一个图片
            alts = img.get('alt')
            alt = re.sub(r'[\?？!！，,\.。、 （）/\*\%]', '', alts)
            # os模块可以分割 . 后面的后缀
            suffixs = os.path.splitext(img_url)[1]
            suffix = re.sub('!dta', '', suffixs)
            filename = alt + suffix
            # 保存图片下来，可以非常方便下载文件或者图片
            # request.urlretrieve(img_url, 'images/' + filename)
            # print(filename)
            self.img_queue.put([img_url, filename])


class Consumer(threading.Thread):
    # 构造函数
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # 重写init函数 需要调用父类的init函数
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            # 如果没有数据
            if self.page_queue.empty() and self.img_queue.empty():
                break
            # 解包
            img_url, filename = self.img_queue.get()
            # print(img_url)
            request.urlretrieve(img_url, 'images/' + filename)
            print(filename+'===下载完成')


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    for x in range(1, 21):
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    for x in range(15):
        t = Procuder(page_queue, img_queue)
        t.start()

    for x in range(15):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
