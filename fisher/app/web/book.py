"""
    Created by 朝南而行 2018/12/5 16:36
"""
from flask import jsonify, request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from app.web import web
from app.forms.book import SearchForm
import json

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
    books = BookCollection()
    # 如果效验通过
    if form.validate():
        # .strip()兼容用户在前后输入空格
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)

            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            yushu_book.search_by_keyword(q, page)

            # result = YuShuBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)
            # dict 序列化
            # API
        books.fill(yushu_book, q)

        # json 直接jsonify(books)
        # object 看下面
        # return jsonify(books)
        # return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False),  200, {'content-type': 'application/json'}
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('关键字输入不符合要求，请重新输入关键字', category='error')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 22
    }
    r1 = {
        'name': '朝南而行',
        'age': 22
    }
    # 消息闪现
    flash('消息闪现666', category='1')
    flash('消息闪现888', category='2')
    # 模板
    return render_template('test.html', data=r, data1=r1)


@web.route('/book/detail/<isbn>')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])



