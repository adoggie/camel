#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Geo_Code(db.Model):
    __tablename__ = 'Geo_Code'
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    ad_code = db.Column('ad_code',db.String(6))
    ad_name = db.Column('ad_name',db.String(256))
    ad_type = db.Column('ad_type',db.Integer)

    def __init__(self,ad_code,ad_name,ad_type):
        self.ad_code = ad_code
        self.ad_name = ad_name
        self.ad_type = ad_type

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
