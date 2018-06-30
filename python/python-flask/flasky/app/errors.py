#coding=utf-8
from flask import render_template
from . import app_blueprint

#自定义404出错页面
@app_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#自定义500出错页面
@app_blueprint.app_errorhandler(404)
def internal_server_error(e):
    return render_template('500.html'),500