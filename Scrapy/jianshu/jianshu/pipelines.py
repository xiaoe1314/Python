# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

# 自学版
# class JianshuPipeline(object):
#     def __init__(self):
#         self.db = pymysql.connect(
#             host="127.0.0.1",
#             user='root',
#             password='root',
#             database='jianshu',
#             port=3306
#         )
#
#     def process_item(self, item, spider):
#         cursor = self.db.cursor()
#         sql = """
#         insert into jianshu_detail(
#             id,title,avatar,author,pub_time,origin_url,author_id,content
#           )
#           values(null,%s,%s,%s,%s,%s,%s,%s);
#         """
#         cursor.execute(sql, (
#             item['title'],
#             item['avatar'],
#             item['author'],
#             item['pub_time'],
#             item['origin_url'],
#             item['author_id'],
#             item['content']))
#         self.db.commit()
#         return item

# 教师版
class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host': "127.0.0.1",
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.db = pymysql.connect(**dbparams)
        self.cursor = self.db.cursor()
        self._sql = None

    # 定义一个属性(将方法变成一个属性)
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into jianshu_detail(
                id,title,avatar,author,pub_time,origin_url,author_id,content
              )
              values(null,%s,%s,%s,%s,%s,%s,%s);
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (
            item['title'],
            item['avatar'],
            item['author'],
            item['pub_time'],
            item['origin_url'],
            item['author_id'],
            item['content']))
        self.db.commit()
        return item

# 插入数据异步版
class JianshuTwistedPipeline(object):
    def __init__(self):

        dbparams = {
            'host': "127.0.0.1",
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    # 定义一个属性(将方法变成一个属性)
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into jianshu_detail(
                id,title,avatar,author,pub_time,origin_url,author_id,content
              )
              values(null,%s,%s,%s,%s,%s,%s,%s);
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (
            item['title'],
            item['avatar'],
            item['author'],
            item['pub_time'],
            item['origin_url'],
            item['author_id'],
            item['content']))

    def handle_error(self, error, item, spider):
        print('*'*10 + error + '*'*10)
        print(error)
        print('*'*10 + error + '*'*10)










