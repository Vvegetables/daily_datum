#coding=utf-8
from alembic.autogenerate import render
from flask import render_template
from flask.globals import request
from flask.helpers import url_for, flash
from flask_login.utils import login_user, login_required, logout_user
from werkzeug import redirect

from app.auth.forms import LoginForm
from app.models import User

from . import auth


@auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('login.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
        