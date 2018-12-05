"""
    Created by 朝南而行 2018/12/5 16:36
"""

from httper import HTTP


class YuShuBook:
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
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        # dist 返回的是字典
        return result
