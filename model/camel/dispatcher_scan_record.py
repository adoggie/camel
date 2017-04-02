#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-08-16"

import sys
import datetime
from instance.camel_app import db
from model.user import User
from model.transport_location import Transport_Location
from model.transport_protocol import Transport_Protocol

class Dispatcher_Scan_Record(db.Model):
    __tablename__ = 'Dispatcher_Scan_Record'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    driver_username = db.Column('driver_username',db.String(11),index=True)
    scan_type = db.Column(db.Integer)
    fk_location_code = db.Column(db.String(6),db.ForeignKey("Transport_Location.code"))
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    fk_trans_number = db.Column(db.String(15),db.ForeignKey("Transport_Protocol.trans_number"))
    upload_time = db.Column('upload_time',db.TIMESTAMP)
    create_at = db.Column(db.TIMESTAMP,default=datetime.datetime.now())
    longitude = db.Column('longitude', db.String(20))
    latitude = db.Column('latitude', db.String(20))
    zh_gps = db.Column('zh_gps', db.String(128))


    operator = db.relationship("User",uselist=False)
    location = db.relationship("Transport_Location",uselist=False,foreign_keys=[fk_location_code])
    transport = db.relationship("Transport_Protocol",uselist=False,foreign_keys=[fk_trans_number])
    
    

    def __init__(self,driver_username,scan_type,fk_location_code,fk_operator_id,fk_trans_number,upload_time,longitude=None, latitude=None, zh_gps=None):
        self.driver_username = driver_username
        self.scan_type = scan_type
        self.fk_location_code = fk_location_code
        self.fk_operator_id = fk_operator_id
        self.fk_trans_number = fk_trans_number
        self.upload_time = upload_time
        self.create_at = datetime.datetime.now()
        if longitude is not None:
            self.longitude = longitude
            self.latitude = latitude
        if zh_gps is not None:
            self.zh_gps = zh_gps



    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        if 'zh_gps' in dict:
            del dict['zh_gps']
        if 'longitude' in dict:
            del dict['longitude']
        if 'latitude' in dict:
            del dict['latitude']
        return dict 
