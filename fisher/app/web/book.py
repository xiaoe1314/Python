"""
    Created by 朝南而行 2018/12/5 16:36
"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web
import json


# <q>/<page> 添加参数
@web.route('/book/search/<num>')
def search(num):
    """
        q: 普通关键词 isbn
        page:
    """
    # 兼容用户在前后输入空格
    num_key = num.strip()
    isbn_or_key = is_isbn_or_key(num_key)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(num_key)
    else:
        result = YuShuBook.search_by_keyword(num_key)
        # dict 序列化
        # API
    # return jsonify(result)
    return json.dumps(result, ensure_ascii=False), 200, {'content-type': 'application/json'}
