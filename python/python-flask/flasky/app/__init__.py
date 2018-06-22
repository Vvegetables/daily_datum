#coding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

#创建蓝本，解决app运行时创建的问题
from flask.blueprints import Blueprint
app_blueprint = Blueprint('app',__name__)
from . import views,errors

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    app.register_blueprint(app_blueprint)
    return app