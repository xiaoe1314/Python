"""
    Created by 朝南而行 2018/12/5 16:36
"""

from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        # url = YuShuBook.isbn_url.format(isbn)
        # 链式查找
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dist 返回的是字典
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        # dist 返回的是字典
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']











