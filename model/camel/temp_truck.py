#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-04-09"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Temp_Truck(db.Model):
    __tablename__ = "Temp_Truck"

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    plate = db.Column('plate',db.String(8),nullable=False)
    length = db.Column(db.FLOAT)
    weight = db.Column(db.FLOAT)
    volume = db.Column(db.FLOAT)
    type = db.Column(db.Integer)
    run_mode = db.Column(db.Integer)
    carrier_type = db.Column(db.Integer)
    qr_code = db.Column(db.String(8))
    content = db.Column('content', db.TEXT)
    fk_trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))

    def __init__(self,plate,length,weight,volume,type,run_mode,carrier_type,qr_code,content,fk_trans_number):
        self.plate = plate
        self.length = length
        self.weight = weight
        self.volume = volume
        self.type = type
        self.run_mode = run_mode
        self.carrier_type = carrier_type
        self.qr_code = qr_code
        self.content = content
        self.fk_trans_number = fk_trans_number

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
