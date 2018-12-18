"""
    Created by 朝南而行 2018/12/7 11:42
"""

from sqlalchemy import Column, Integer, String, Boolean, Float
from app.models.base import db, Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, Base):
    # 1 设置数据库表的名字
    # __tablename__ = 'user1'
    # 1 类型 2 设置为主键 3 自增长
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 1 String类型，限制长度最大为50 2 不允许为空
    nickname = Column(String(24), nullable=False)
    phone_num = Column(String(18), unique=True)
    # 1 设置数据库字段的名字
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # check_password_hash做密码的加密和对比， 相等返回True，不相等返回False
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # def get_id:
    #     pass


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
