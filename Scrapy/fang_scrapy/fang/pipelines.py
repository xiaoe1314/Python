# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class FangPipeline(object):
    def __init__(self):
        self.new_house_fp = open('new_house.json', 'wb')
        self.esf_fp = open('esf.json', 'wb')
        self.new_house_exporter = JsonLinesItemExporter(self.new_house_fp, ensure_ascii=False)
        self.esf_exporter = JsonLinesItemExporter(self.esf_fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.new_house_exporter.export_item(item)
        self.esf_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.new_house_fp.close()
        self.esf_fp.close()




















