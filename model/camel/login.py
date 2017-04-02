#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Login(db.Model):
    __tablename__ = "Login"

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    token = db.Column('token',db.String(36))
    device_id = db.Column('device_id',db.String(36))
    app_ver = db.Column('app_ver',db.String(16))
    device_type = db.Column('device_type',db.Integer)
    login_type = db.Column('login_type',db.Integer)
    login_time = db.Column('login_time',db.TIMESTAMP,default = datetime.datetime.now())
    user_id = db.Column(db.Integer,db.ForeignKey("User.id"))

    def __init__(self,token,user_id,device_id,app_ver,device_type,login_type):
        self.token = token
        self.user_id = user_id
        self.device_id = device_id
        self.app_ver = app_ver
        self.device_type = device_type
        self.login_type = login_type
        self.login_time = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
