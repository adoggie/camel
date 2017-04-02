#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-05-28"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Truck(db.Model):
    __tablename__ = "Truck"

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    plate = db.Column('plate',db.String(8))
    vehicle_no = db.Column('vehicle_no',db.String(45))
    length = db.Column(db.FLOAT)
    wide = db.Column(db.FLOAT)
    high = db.Column(db.FLOAT)
    weight = db.Column(db.FLOAT)
    volume = db.Column(db.FLOAT)
    type = db.Column(db.Integer)
    run_mode = db.Column(db.Integer)
    vehicle_type = db.Column(db.String(45))
    qr_code = db.Column(db.String(8))
    line_property = db.Column('line_property',db.String(45))
    is_temp_truck = db.Column(db.Integer)
    is_forbidden = db.Column(db.Integer)
    org_code = db.Column(db.String(6))
    carrier_name = db.Column(db.String(512))
    carrier_code = db.Column(db.String(45))
    #fk_carrier_id = db.Column(db.Integer,db.ForeignKey("Carrier.id"))
    if_valid= db.Column(db.Integer)
    create_time = db.Column('create_time',db.TIMESTAMP,default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP)
    trailers = db.Column(db.Integer)
    is_onway = db.Column(db.Integer,default=0)

    def __init__(self,plate,vehicle_no,length,wide,high,weight,volume,type,vehicle_type,run_mode,qr_code,line_property,is_temp_truck,is_forbidden,org_code,carrier_name,carrier_code,if_valid,trailers):
        self.plate = plate
        self.vehicle_no = vehicle_no
        self.length = length
        self.wide = wide
        self.high = high
        self.weight = weight
        self.volume = volume
        self.type = type
        self.vehicle_type = vehicle_type
        self.run_mode = run_mode
        self.qr_code = qr_code
        self.line_property = line_property
        self.is_temp_truck = is_temp_truck
        self.is_forbidden = is_forbidden
        self.org_code = org_code
        self.carrier_name = carrier_name
        self.carrier_code = carrier_code
        self.if_valid = if_valid 
        self.create_time = datetime.datetime.now()
        self.trailers = trailers

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
