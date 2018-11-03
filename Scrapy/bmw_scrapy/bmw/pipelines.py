# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


# 启动这个pipline需要在setting里面将注释取消
class BmwPipeline(object):

    def __init__(self):
        # os.path.join 拼接路径  os.path.dirname(__file__)查询当前文件路径
        self.images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
        # os.path.exists判断路径是否存在
        if not os.path.exists(self.images_path):
            os.mkdir(self.images_path)

    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']
        category_path = os.path.join(self.images_path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            url_name = url.split('_')[-1]
            request.urlretrieve(url,os.path.join(category_path,url_name))
        return item
