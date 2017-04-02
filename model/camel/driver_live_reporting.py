#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from sqlalchemy.orm import backref
from instance.camel_app import db

class Driver_Live_Reporting(db.Model):
    __tablename__ = "Driver_Live_Reporting"

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    photo_urls = db.Column('photo_urls',db.TEXT)#json array
    content = db.Column('content',db.TEXT)
    create_at = db.Column('create_at',db.TIMESTAMP,default = datetime.datetime.now())
    report_type = db.Column('report_type',db.Integer)
    fk_trans_number = db.Column('fk_trans_number',db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    uuid = db.Column('uuid',db.String(36))
    s_lon = db.Column('s_lon',db.Integer)
    s_lat = db.Column('s_lat',db.Integer)
    start_time = db.Column(db.String(256))
    s_address = db.Column(db.String(256))
    e_lon = db.Column('e_lon',db.Integer)
    e_lat = db.Column('e_lat',db.Integer)
    end_time = db.Column(db.String(256))
    e_address = db.Column(db.String(256))
    fk_user_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    flag = db.Column('flag',db.String(8))

    user = db.relationship("User",backref=backref("Driver_Live_Reporting",uselist=False),foreign_keys = [fk_user_id])

    def __init__(self,photo_urls,content,report_type,fk_trans_number,uuid,fk_user_id,s_lon,s_lat,start_time,s_address,e_lon=None,e_lat=None,end_time=None,e_address=None,flag=None):
        self.photo_urls = photo_urls
        self.content = content
        self.create_at = datetime.datetime.now()
        self.report_type = report_type
        self.fk_trans_number = fk_trans_number
        self.uuid = uuid
        self.fk_user_id = fk_user_id
        self.s_lon = s_lon
        self.s_lat = s_lat
        self.start_time = start_time
        self.s_address = s_address
        if e_lon:
            self.e_lon = e_lon
        if e_lat:
            self.e_lat = e_lat
        if end_time:
            self.end_time = end_time
        if e_address:
            self.e_address = e_address
        self.flag = flag

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
