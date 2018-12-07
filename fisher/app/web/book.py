"""
    Created by 朝南而行 2018/12/5 16:36
"""
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web import web
from app.forms.book import SearchForm


# <q>/<page> 添加参数
# @web.route('/book/search/<num>/<page>')
# def search(num, page):

@web.route('/book/search')
def search():
    """
        q: 普通关键词 isbn
        page:
    """
    # flask 中来验证客户端传过来的参数
    # 使用第三方插件进行参数效验
    # 查询参数 POST参数 remote ip 效验
    # num = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    # 如果效验通过
    if form.validate():
        # .strip()兼容用户在前后输入空格
        p = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(p)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(p)
        else:
            result = YuShuBook.search_by_keyword(p, page)
            # dict 序列化
            # API
        return jsonify(result)
        # return json.dumps(result, ensure_ascii=False), 200, {'content-type': 'application/json'}
    else:
        return jsonify(form.errors)
