#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email',validator=[Required(),Length(1,64),Email()])
    password = PasswordField('password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('log in')

