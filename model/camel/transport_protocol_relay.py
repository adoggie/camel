#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-03-09"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Transport_Protocol_Relay(db.Model):
    __tablename__ = 'Transport_Protocol_Relay'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    create_at = db.Column(db.TIMESTAMP)
    trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    start_time = db.Column('start_time',db.String(16))
    end_time = db.Column('end_time',db.String(16))
    index = db.Column(db.Integer)
    location_code = db.Column(db.String(6),db.ForeignKey("Transport_Location.code"))
    location_code_type = db.Column(db.Integer)

    location = db.relationship("Transport_Location",uselist=False,foreign_keys = [location_code])

    def __init__(self,trans_number,location_code,start_time,end_time,index,location_code_type):
        self.create_at = datetime.datetime.now()
        self.trans_number = trans_number
        self.location_code = location_code
        self.start_time = start_time
        self.end_time = end_time
        self.index = index
        self.location_code_type = location_code_type

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
