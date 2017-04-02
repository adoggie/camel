#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-28"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Cargo(db.Model):
    __tablename__ = 'Cargo'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    name = db.Column('name',db.String(256))
    number = db.Column('number',db.Integer)
    packing_type = db.Column('packing_type',db.Integer)
    weight = db.Column('weight',db.FLOAT)
    type = db.Column('type',db.Integer)
    note = db.Column('note',db.TEXT)
    fk_bill_number = db.Column('fk_bill_number',db.String(24),db.ForeignKey("Logistics_Bill_Desc.bill_number"))

    def __init__(self,name,number,packing_type,weight,type,fk_bill_number,note):
        self.name = name
        self.number = number
        self.packing_type = packing_type
        self.weight = weight
        self.type = type
        self.fk_bill_number = fk_bill_number
        self.note = note

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
