#coding = utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for #url_for 是根据路由名字获得路由路径的函数
from . import app_blueprint

from .forms import NameForm

from . import db

from .models import User

@app_blueprint.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
    form.name.data = ''
    return render_template('index.html', form=form, name=name)