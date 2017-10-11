# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField
from wtforms.validators import Required,Length,Email,Regexp
from ..models import Role,User
from flask_pagedown.fields import PageDownField

class NameForm(FlaskForm):
    name = StringField(u'你的名字',validators=[Required()])
    submit = SubmitField(u'确定')


class EditProfieForm(FlaskForm):
    name = StringField(u'昵称',validators=[Length(0,64)])
    location = StringField(u'地址',validators=[Length(0,64)])
    about_me = TextAreaField(u'个性签名')
    submit = SubmitField(u'提交')

class EditProfieAdminForm(FlaskForm):
    email = StringField(u'邮箱',validators=[Required(),Length(1,64),Email()])
    username = StringField(u'用户名',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,u'用户名必须只有字母,数字，.，和下划线')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role',coerce=int)
    name = StringField(u'昵称',validators=[Length(0,64)])
    location = StringField(u'地址',validators=[Length(0,64)])
    about_me = TextAreaField(u'个性签名')
    submit = SubmitField(u'提交')

    def __init__(self,user,*args,**kwargs):

        super(EditProfieAdminForm,self).__init__(*args,**kwargs)
        self.role.choices = [(role.id,role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def valideate_email(self,field):
        if field.data != self.user.username and \
            User.query.filter_by(username=field.data).first():
            raise ValueError('用户名已在使用')

class PostForm(FlaskForm):
    body = PageDownField(u'发表文章',validators=[Required()])
    submit = SubmitField(u'确定')

class CommentForm(FlaskForm):
    body = StringField('',validators=[Required()])
    submit = SubmitField(u'确定')