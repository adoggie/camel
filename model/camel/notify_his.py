#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Notify_His(db.Model):
    __tablename__ = 'Notify_His'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    message = db.Column('message',db.TEXT)
    message_type = db.Column('message_type',db.Integer)
    push_type = db.Column('push_type',db.Integer)
    push_time = db.Column('push_time',db.TIMESTAMP,default = datetime.datetime.now())
    is_fail = db.Column('is_fail',db.BOOLEAN)
    fk_trans_number = db.Column('fk_trans_number',db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))

    def __init__(self,message,message_type,push_type,push_time,is_fail,fk_trans_number):
        self.message = message
        self.message_type = message_type
        self.push_type = push_type
        self.push_time = push_time
        self.is_fail = is_fail
        self.fk_trans_number = fk_trans_number
        self.push_time = datetime.datetime.now() 

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
