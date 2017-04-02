#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.user import User

class Transport_Protocol_Flow(db.Model):
    __tablename__ = 'Transport_Protocol_Flow'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    status = db.Column(db.Integer)
    status_time = db.Column(db.TIMESTAMP)
    lon = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    address = db.Column(db.TEXT)
    create_at = db.Column(db.TIMESTAMP,default=datetime.datetime.now())
    fk_trans_number = db.Column(db.String(15),db.ForeignKey("Transport_Protocol.trans_number"))
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    operator = db.relationship("User",uselist=False)
    content = db.Column('content',db.TEXT)

    def __init__(self,status,status_time,lon,lat,fk_trans_number,fk_operator_id,address,content=None):
        self.status = status
        self.status_time = status_time
        if lon:
            self.lon = lon
        if lat:
            self.lat = lat
        self.fk_trans_number = fk_trans_number
        self.fk_operator_id = fk_operator_id
        self.address = address
        self.create_at = datetime.datetime.now()
        self.content = content

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
