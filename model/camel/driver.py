#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from sqlalchemy.orm import backref
from instance.camel_app import db
from model.truck import Truck
from model.user import User

class Driver(db.Model):
    __tablename__ = 'Driver'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_user_id = db.Column('fk_user_id',db.Integer,db.ForeignKey("User.id"))
    plate = db.Column('plate',db.String(7),db.ForeignKey("Truck.plate"))
    create_at = db.Column(db.TIMESTAMP,default = datetime.datetime.now())
    fk_carrier_id = db.Column(db.Integer,db.ForeignKey("Carrier.id"))
    
    user = db.relationship("User",backref=backref("Driver",uselist=False),foreign_keys = [fk_user_id])

    def __init__(self,user_id,plate,carrier_id=None):
        self.fk_user_id = user_id
        self.plate = plate
        self.create_at = datetime.datetime.now()
        self.fk_carrier_id = carrier_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
