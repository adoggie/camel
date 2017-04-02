#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-04-08"

import sys
import datetime
from sqlalchemy.orm import backref
from instance.camel_app import db

class RS_LT_Truck(db.Model):
    __tablename__ = "RS_LT_Truck"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    qr_code = db.Column(db.String(8),db.ForeignKey("Truck.qr_code"))
    line_no = db.Column(db.String(256),db.ForeignKey("Line.line_no"))

    truck = db.relationship("Truck",backref=backref("RS_LT_Truck",uselist=False),foreign_keys = [qr_code])
    line = db.relationship("Line",backref=backref("RS_LT_Truck",uselist=False),foreign_keys = [line_no])

    def __init__(self,qr_code,line_no):
        self.qr_code = qr_code
        self.line_no = line_no

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
