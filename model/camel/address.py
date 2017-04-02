#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-28"

import datetime

from camel.biz.application.flasksrv import db

class Address(db.Model):
    __tablename__ = 'Address'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    address = db.Column('address',db.TEXT)
    road_address = db.Column('road_address',db.TEXT)   
    lon = db.Column('lon',db.Integer)
    lat = db.Column('lat',db.Integer)
    fk_bill_number = db.Column('fk_bill_number',db.String(24),db.ForeignKey("Logistics_Bill_Desc.bill_number"))
    fk_province_code = db.Column('fk_province_code',db.String(6),db.ForeignKey("Geo_Code.ad_code"))
    fk_city_code = db.Column('fk_city_code',db.String(6),db.ForeignKey("Geo_Code.ad_code"))
    fk_area_code = db.Column('fk_area_code',db.String(6),db.ForeignKey("Geo_Code.ad_code"))
    create_at = db.Column('create_at',db.TIMESTAMP,default = datetime.datetime.now())

    def __init__(self,address,road_address,lon,lat,fk_bill_number,fk_province_code,fk_city_code,fk_area_code):
        self.address = address
        self.road_address = road_address
        self.lon = lon
        self.lat = lat
        self.fk_bill_number = fk_bill_number
        self.fk_province_code = fk_province_code
        self.fk_city_code = fk_city_code
        self.fk_area_code = fk_area_code
        self.create_at = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
