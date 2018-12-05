"""
    Created by 朝南而行 2018/12/5 16:36
"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web


# <q>/<page> 添加参数
@web.route('/book/search/<num>')
def search(num):
    """
        q: 普通关键词 isbn
        page:
    """
    isbn_or_key = is_isbn_or_key(num)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(num)
    else:
        result = YuShuBook.search_by_keyword(num)
        # dict 序列化
        # API
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
