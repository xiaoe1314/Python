"""
    Created by 朝南而行 2018/12/7 10:45
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(DataRequired(), validators=[Length(min=1, max=30, message='字段长度必须介于1到30个字符之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

