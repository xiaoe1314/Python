"""
    Created by 朝南而行 2018/12/5 17:55
"""
from . import web


@web.route('/user/login')
def login():
    return '这个是登录页面'
