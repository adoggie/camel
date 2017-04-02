#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-02-25"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Carrier(db.Model):
    __tablename__ = 'Carrier'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    carrier_name = db.Column('carrier_name',db.String(256))
    drivers = db.relationship("Driver",lazy="dynamic")
    trucks = db.relationship("Truck",lazy="dynamic")

    def __init__(self,name):
        self.carrier_name = name

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
