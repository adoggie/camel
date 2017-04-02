#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
#sys.path.append("..")
from instance.camel_app import db
from model.login import Login

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    hash = db.Column('hash',db.String(256),nullable=False)
    email = db.Column('email',db.String(64))
    mobile = db.Column('mobile',db.String(11))
    telephone = db.Column('telephone',db.String(11))
    role_type = db.Column('role_type',db.Integer,nullable=False)
    active = db.Column('active',db.Integer,default=0)
    create_time = db.Column('create_time',db.TIMESTAMP,default=datetime.datetime.now())
    username = db.Column('username',db.String(32),index=True,unique=True)
    fullname = db.Column('fullname',db.String(32))
    photo_url = db.Column('photo_url',db.TEXT)
    zh_name = db.Column('zh_name',db.String(32))
    user_no = db.Column('user_no',db.String(32),index=True,unique=True)
    registration_id = db.Column('registration_id',db.String(36))
    fk_location_code = db.Column(db.Integer)
    fk_dept_id = db.Column(db.Integer)
    login_his = db.relationship("Login")
    update_time = db.Column('update_time',db.TIMESTAMP)

    def __init__(self,username,password,email,mobile,telephone,role_type,fullname,
            photo_url,active,user_no,registration_id,fk_location_code):
        self.username = username
        m2 = hashlib.md5()
        m2.update(password)
        self.hash = m2.hexdigest()
        self.email = email
        self.mobile = mobile
        self.telephone = telephone
        self.role_type = role_type
        self.fullname = fullname
        self.photo_url = photo_url
        self.active = active
        self.create_time = datetime.datetime.now()
        self.zh_name = fullname
        self.user_no = user_no
	self.registration_id = registration_id
        self.fk_location_code = fk_location_code

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
