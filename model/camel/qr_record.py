#-*- coding:utf-8 -*-
__author__ = "zc"
__date__ = "2016-05-09"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.user import User
from model.driver import Driver
from model.truck import Truck

class QR_Record(db.Model):
    __tablename__ = 'QR_Record'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_driver_id = db.Column('fk_driver_id',db.Integer,db.ForeignKey("Driver.id"))
    plate = db.Column(db.String(8),db.ForeignKey("Truck.plate"))
    fk_trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    operator_type = db.Column('operator_type',db.Integer)
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    create_time = db.Column(db.TIMESTAMP,default=datetime.datetime.now())

    operator = db.relationship("User",uselist=False,foreign_keys=[fk_operator_id])

    def __init__(self,fk_driver_id,plate,fk_trans_number,operator_type,fk_operator_id):
        self.fk_trans_number = fk_trans_number
        self.plate = plate
        self.fk_driver_id = fk_driver_id
	self.operator_type = operator_type
        self.fk_operator_id = fk_operator_id
        self.create_time = datetime.datetime.now()
    
    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
