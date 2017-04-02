#-*- coding:utf-8 -*-
__author__ = "Bo"
__date__ = "2016-03-02"

import sys
import datetime
from instance.camel_app import db

class RS_CQ_Trans(db.Model):
    __tablename__ = "RS_CQ_Trans"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    cq_number = db.Column(db.Integer)
    create_at = db.Column(db.TIMESTAMP,default = datetime.datetime.now())

    def __init__(self,trans_number,cq_number):
        self.trans_number = trans_number
        self.cq_number = cq_number
        self.create_at = datetime.datetime.now() 

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
