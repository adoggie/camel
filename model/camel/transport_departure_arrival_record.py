#-*- coding:utf-8 -*-
__author__ = "Bo"
__date__ = "2016-02-18"

import sys
import hashlib
import datetime
import time
from instance.camel_app import db

class Transport_Departure_Arrival_Record(db.Model):
    __tablename__ = 'Transport_Departure_Arrival_Record'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    trans_number = db.Column(db.String(24))
    plate = db.Column(db.String(8))
    create_at= db.Column(db.TIMESTAMP)
    status_time= db.Column(db.TIMESTAMP)
    type = db.Column(db.Integer)
    lon = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    address = db.Column(db.TEXT)
    fk_driver_id = db.Column(db.Integer,db.ForeignKey('Driver.id'))
    fk_location_code = db.Column(db.String(6),db.ForeignKey('Transport_Location.code'))
    fk_operator_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    source_type = db.Column(db.Integer)
    jg_trigger_time = db.Column(db.TIMESTAMP)
    location = db.relationship("Transport_Location",uselist=False,foreign_keys=[fk_location_code])

    def __init__(self,trans_number,plate,type,lon,lat,address,fk_driver_id,fk_location_code,fk_operator_id,source_type=None,status_time=None):
        self.trans_number = trans_number
        self.plate = plate
        self.type = type
        self.lon = lon
        self.lat = lat
        self.address = address
        self.fk_driver_id = fk_driver_id
        self.fk_location_code = fk_location_code
        self.fk_operator_id = fk_operator_id
        self.source_type = source_type
        if status_time:
            self.status_time = status_time
            if source_type and int(source_type) == 3:
                self.jg_trigger_time = int(time.mktime(status_time.timetuple()))
        else:
            self.status_time = datetime.datetime.now()
    
    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
