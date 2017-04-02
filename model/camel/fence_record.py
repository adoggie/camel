#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-29"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Fence_Record(db.Model):
    __tablename__ = "Fence_Record"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    fence_name = db.Column(db.String(256))
    trigger_time = db.Column(db.TIMESTAMP)
    trigger_type = db.Column(db.Integer)
    action = db.Column(db.Integer)
    create_at = db.Column(db.TIMESTAMP)
    fk_trans_number = db.Column(db.String(24))

    def __init__(self,fence_name,trigger_time,trigger_type,action,trans_number):
        self.fence_name = fence_name
        self.trigger_time = trigger_time
        self.trigger_type = trigger_type
        self.action = action
        self.fk_trans_number = trans_number
        self.create_at = datetime.datetime.now() 

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
