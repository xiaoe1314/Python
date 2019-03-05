"""
    Created by 朝南而行 2019/1/21 15:08
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class CustomURL(Form):
    custom_url = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
    custom_json = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

