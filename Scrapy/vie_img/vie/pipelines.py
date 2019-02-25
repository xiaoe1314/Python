# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from contextlib import closing


class ViePipeline(object):
    def __init__(self):
        # __file__ 当前文件的目录
        # os.path.dirname 相当于 cd ..
        # os.path.join 路径的拼接
        # os.path.exists 判断路径是否存在，如果path存在，返回True；如果path不存在，返回False
        self.path = os.path.join(os.path.dirname(__file__), 'mp4')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            print('路径不存在')
        else:
            print('路径存在')
    
    def process_item(self, item, spider):
        base_url = item['base_url']
        filename = item['filename']
        
        with closing(requests.get(base_url, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            data_count = 0
            with open(os.path.join(self.path, filename), "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    data_count = data_count + len(data)
                    now_jd = (data_count / content_size) * 100
                    print("\r 文件下载进度：%d%%(%d/%d) - %s" %
                          (now_jd, data_count, content_size, base_url), end=" ")
