"""
    Created by 朝南而行 2018/12/5 16:36
"""

from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    # 构造器
    def __init__(self):
        # 实例变量
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        # url = YuShuBook.isbn_url.format(isbn)
        # 链式查找（先从实例变量里面查找，如果没有则查找类变量）
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        # 在获取到数据的时候，查询数据库有没有数据，如果有直接返回，如果没有则存到数据库
        # if book:
        #    return book
        # else:
        #     save(result)
        self.__fill_single(result)
        # dist 返回的是字典
        # return result

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        # dist 返回的是字典
        # return result

    def calculate_start(self, page):
        return (page-1) * current_app.config['PER_PAGE']

    # 在self.books如果没有数据的时候，直接返回self.books[0]会报错，用这样的表达式比较好
    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None










