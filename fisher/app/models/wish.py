"""
    Created by 朝南而行 2018/12/18 15:05
"""


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.models.base import db, Base
from sqlalchemy.orm import relationship


class Wish(Base):
    # 1 类型 2 设置为主键
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # uid表示是user下面的id
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    # 礼物有没有送出去
    launched = Column(Boolean, default=False)

