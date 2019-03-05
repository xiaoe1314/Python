"""
    Created by 朝南而行 2018/12/26 11:14
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
