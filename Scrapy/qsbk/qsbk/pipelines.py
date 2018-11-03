# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json

# class QsbkPipeline(object):
#     def __init__(self):
#         # 打开文件
#         self.fp = open("duanzi.json", "w", encoding='utf-8')
#
#     # 爬虫打开后就会调用这个函数
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     # item 是爬虫传过来的数据
#     def process_item(self, item, spider):
#         # QsbkItem转换成字典dict(item)
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         # 写入文件中
#         self.fp.write(item_json+'\n')
#         return item
#
#     # 爬虫完成后就会调用这个函数
#     def close_spider(self, spider):
#         # 关闭文件
#         self.fp.close()

# from scrapy.exporters import JsonItemExporter
# # scrapy 框架的导出器
# class QsbkPipeline(object):
#     def __init__(self):
#         # 已二进制打开文件
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     # 爬虫打开后就会调用这个函数
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     # item 是爬虫传过来的数据
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     # 爬虫完成后就会调用这个函数
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         # 关闭文件
#         self.fp.close()
#         print('爬虫结束了')

from scrapy.exporters import JsonLinesItemExporter
# scrapy 框架的导出器
class QsbkPipeline(object):
    def __init__(self):
        # 已二进制打开文件
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    # 爬虫打开后就会调用这个函数
    def open_spider(self, spider):
        print('爬虫开始了')

    # item 是爬虫传过来的数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # 爬虫完成后就会调用这个函数
    def close_spider(self, spider):
        # 关闭文件
        self.fp.close()
        print('爬虫结束了')

