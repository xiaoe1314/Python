"""
    Created by 朝南而行 2018/12/17 16:36
"""
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User


class LoginForm(Form):
    email = StringField(DataRequired(),
                        validators=[Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[Length(6, 32),
                                         DataRequired(message='密码不可以为空，请输入你的密码')])


class RegisterForm(LoginForm):
    email = StringField(DataRequired(),
                        validators=[Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[Length(6, 32),
                                         DataRequired(message='密码不可以为空，请输入你的密码')])

    nickname = StringField(validators=[DataRequired(),
                                       Length(min=2, max=10, message='昵称至少需要两个字符，最多10个字符')])

    # 业务的效验
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')









