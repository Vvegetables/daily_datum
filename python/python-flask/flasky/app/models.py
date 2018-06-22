#coding=utf-8
from flask_sqlalchemy.model import Model
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


class Role(Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    
    def __repr__(self):
        return '<Role %r>' % self.name


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username