#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.geo_code import Geo_Code

class Transport_Location(db.Model):
    __tablename__ = 'Transport_Location'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(256))
    address = db.Column(db.TEXT)
    road_address = db.Column(db.TEXT)
    radius_b = db.Column(db.Integer)
    radius_s = db.Column(db.Integer)
    lon = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    fk_province_code = db.Column(db.String(6),db.ForeignKey('Geo_Code.ad_code'))
    fk_city_code = db.Column(db.String(6),db.ForeignKey('Geo_Code.ad_code'))
    fk_area_code = db.Column(db.String(6),db.ForeignKey('Geo_Code.ad_code'))
    code = db.Column(db.String(6))
    child_code = db.Column(db.String(2))
    contact  = db.Column(db.String(24))
    telephone = db.Column(db.String(11))
    province = db.relationship("Geo_Code",uselist=False,foreign_keys=[fk_province_code])
    city = db.relationship("Geo_Code",uselist=False,foreign_keys=[fk_city_code])
    area = db.relationship("Geo_Code",uselist=False,foreign_keys=[fk_area_code])
    create_time = db.Column('create_time',db.TIMESTAMP,default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP)

    def __init__(self,name,address,road_address,radius_b,radius_s,lon,lat,fk_province_code,fk_city_code,fk_area_code,code,child_code,contact,telephone):
        self.name = name
        self.address = address
        self.road_address = road_address
        self.radius_b = radius_b
        self.radius_s = radius_s
        self.lon = lon
        self.lat = lat
        self.fk_province_code = fk_province_code
        self.fk_city_code = fk_city_code
        self.fk_area_code = fk_area_code
        self.code = code
        self.child_code = child_code
        self.contact = contact
        self.telephone = telephone
        self.create_time = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
