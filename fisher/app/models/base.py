"""
    Created by 朝南而行 2018/12/17 16:05
"""
from sqlalchemy import Column, Integer, SmallInteger
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy
# Flask_SQLAlchemy
# 如何把book模型映射到数据库中去
# 1 需要Flask_SQLAlchemy 核心对象
# 2 实例化 Flask_SQLAlchemy
# 3 要插入到app 核心对象上
db = SQLAlchemy()


class Base(db.Model):
    # 基类不需要创建成表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 删除数据, 操作删除数据只是状态的改变，而不是删除数据库数据
    status = Column(SmallInteger, default=1)

    # 如果字典里面某一个key和模型里某一个属性是相同的，我们就把key对应的值赋值给模型里的属性
    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # 一个对象下面是否包含一个属性
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


