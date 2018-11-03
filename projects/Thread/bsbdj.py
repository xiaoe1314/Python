

import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

# 实战-百思不得姐之多线程异步爬爬取图片
# 1.获取每一页的url main()函数完成
# 2.生产者（获取每一页的图片url）
# 3.每个表情的url
# 4.消费者（下载图片）


#把队列传进来，需要重写init函数
class Procuder(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
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
            url, x = self.page_queue.get()
            self.parse_page(url, x)

    def parse_page(self, url, x):
        response = requests.get(url=url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='j-r-list-c']//img")
        for img in imgs:
            img_urls = img.get('data-original')

            # 获取图片的名字和获取图片的后缀才能拼接一个图片
            alts = img.get('alt')
            alt = re.sub(r'[\?？!！，\\\n～,\.。、 （）/\*\%《》\😂\😂\😄\😊“”：【】#~…·ԅ(¯﹃\¯\ԅ)|]', '', alts)[0:100]
            # print(str(len(alt))+'==='+alt)
            # os模块可以分割 . 后面的后缀
            suffixs = os.path.splitext(img_urls)[1]

            if len(suffixs) == 0:
                suffix = re.sub('', '.jpg', suffixs)
                filename = alt + suffix
                self.img_queue.put([img_urls, filename, x])
            else:
                filename = alt + suffixs
                self.img_queue.put([img_urls, filename, x])


                # 保存图片下来，可以非常方便下载文件或者图片
                # request.urlretrieve(img_url, 'images/' + filename)
                # self.img_queue.put([img_urls, filename])


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

            img_url, filename, x = self.img_queue.get()

            request.urlretrieve(img_url, 'images/' + str(x) + '/' + filename)
            print(filename+'===下载完成')


# 创建文件夹   mkdir("E:\\Python\\demo01\\Thread\\bb")
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + '目录已存在')
        return False


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    for x in range(1, 51):
        url = 'http://www.budejie.com/pic/%d' % x
        mkdir("E:\\Python\\demo01\\Thread\\images\\%d" % x)
        page_queue.put([url, x])

    for x in range(5):
        t = Procuder(page_queue, img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
