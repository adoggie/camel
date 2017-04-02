#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-02-25"

import sys
import datetime
from sqlalchemy.orm import backref
from instance.camel_app import db

class RS_QR_Driver(db.Model):
    __tablename__ = "RS_QR_Driver"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    qr_code = db.Column(db.String(8),db.ForeignKey("Truck.qr_code"))
    fk_driver_id = db.Column(db.Integer,db.ForeignKey("Driver.id"))
    create_at = db.Column(db.TIMESTAMP,default = datetime.datetime.now())

    truck = db.relationship("Truck",backref=backref("RS_QR_Driver",uselist=False),foreign_keys = [qr_code])
    driver = db.relationship("Driver",backref=backref("RS_QR_Driver",uselist=False),foreign_keys = [fk_driver_id])

    def __init__(self,qr_code,driver_id):
        self.qr_code = qr_code
        self.fk_driver_id = driver_id
        self.create_at = datetime.datetime.now() 

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
