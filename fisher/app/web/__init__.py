"""
    Created by 朝南而行 2018/12/5 17:52
"""

from flask import Blueprint

# 蓝图 blueprint 蓝本
web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
# from app.web import user
