#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-08-28"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Trigger_Record(db.Model):
    '''
        This table stores the valid trigger data.
    '''
    __tablename__ = "Trigger_Record"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    fk_trans_number = db.Column(db.String(24))
    fk_location_code = db.Column(db.String(6))
    fk_child_code = db.Column(db.String(6))
    trigger_time = db.Column(db.TIMESTAMP)
    trigger_type = db.Column(db.Integer)
    comt_type = db.Column(db.Integer)
    operationer = db.Column(db.String(32))
    create_time = db.Column(db.TIMESTAMP,default = datetime.datetime.now())

    def __init__(self,fk_trans_number,fk_location_code,fk_child_code,trigger_time,trigger_type,comt_type,operationer):
        self.fk_trans_number = fk_trans_number
        self.fk_location_code = fk_location_code
        self.fk_child_code = fk_child_code
        self.trigger_time = trigger_time
        self.trigger_type = trigger_type
        self.comt_type = comt_type
        self.operationer = operationer

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
