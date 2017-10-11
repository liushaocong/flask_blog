# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(u'邮箱',validators=[Required(),Length(1,64),Email()])
    password = PasswordField(u'密码',validators=[Required()])
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'确定')

class RegistrationForm(FlaskForm):
    email = StringField(u'邮箱',validators=[Required(),Length(1,64),Email()])
    username = StringField(u'用户名',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,u'用户名必须只有字母,数字，.，和下划线')])
    password = PasswordField(u'密码',validators=[Required(),EqualTo('password2',message=u'密码必须一致')])
    password2 = PasswordField(u'重复密码',validators=[Required()])
    submit = SubmitField(u'确定')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'电子邮件已经注册')

    def validate_name(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已经注册')


