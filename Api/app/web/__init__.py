"""
    Created by 朝南而行 2018/12/26 11:21
"""

from flask import Blueprint


web = Blueprint('web', __name__)

from app.web import home

