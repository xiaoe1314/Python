"""
    Created by 朝南而行 2018/12/5 16:36
"""
from flask import Flask
from app.models.book import db

__author__ = '朝南而行'


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    # 接收模块的路径（载入配置文件, 通过这种方式载入，常量必须要全部大写）
    # DEBUG 默认是False
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # print(app.config['DEBUG'])

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


