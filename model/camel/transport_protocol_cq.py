#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-07-26"

import sys
import datetime
import time
from instance.camel_app import db

class Transport_Protocol_Cq(db.Model):
    __tablename__ = "Transport_Protocol_Cq"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    cq_number = db.Column(db.Integer)
    create_at = db.Column(db.TIMESTAMP)
    #create_at = db.Column(db.TIMESTAMP,default = datetime.datetime.now())
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))

    #def __init__(self,trans_number,cq_number,fk_operator_id,create_at=datetime.datetime.now()):
    def __init__(self,trans_number,cq_number,fk_operator_id):
        self.trans_number = trans_number
        self.cq_number = cq_number
        self.fk_operator_id = fk_operator_id
        #self.create_at = create_at

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
