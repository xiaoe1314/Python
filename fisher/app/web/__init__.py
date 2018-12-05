"""
    Created by 朝南而行 2018/12/5 17:52
"""

from flask import Blueprint

# 蓝图 blueprint 蓝本
web = Blueprint('web', __name__)

from app.web import book
from app.web import user
