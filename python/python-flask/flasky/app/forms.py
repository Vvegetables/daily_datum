#coding = utf-8
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')