#coding:utf-8

from camel.biz.application.flasksrv import db

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Application(db.Model):
    __tablename__ = 'koala_app'
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column( db.String(40),unique=True,nullable=False,index=True)     # 应用名称
    app_id = db.Column(db.String(60),unique=True,nullable=False,index=True)   # 应用标识
    secret_key = db.Column(db.String(200),nullable=False)
    reaml = db.Column(db.String(40),nullable=False,default='',index=True)

class AppUser(db.Model):
    """定义数据模型"""
    __tablename__ = 'koala_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), index=True,unique=True)
    app_id = db.Column( db.Integer, db.ForeignKey('application.id'),index=True)
    app = db.relationship('Application',backref=db.backref('users',lazy = 'dynamic'))


    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User: {}'.format(self.user_id)