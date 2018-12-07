"""
    Created by 朝南而行 2018/12/7 11:42
"""

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy
# Flask_SQLAlchemy
# 如何把book模型映射到数据库中去
# 1 需要Flask_SQLAlchemy 核心对象
# 2 实例化 Flask_SQLAlchemy
# 3 要插入到app 核心对象上
db = SQLAlchemy()


class Book(db.Model):
    # 1 类型 2 设置为主键 3 自增长
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 1 String类型，限制长度最大为50 2 不允许为空
    title = Column(String(50), nullable=False)
    author = Column(String(50), default='无名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    # 1 String类型，限制长度最大为50 2 不允许为空 3 在数据库中只能是唯一值
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
