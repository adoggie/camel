#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-04-08"

import sys
import hashlib
import datetime
from instance.camel_app import db

class Line(db.Model):
    __tablename__ = 'Line'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    line_no = db.Column('line_no',db.String(256))
    line_name = db.Column('line_name',db.String(1000))
    start_org_code = db.Column('start_org_code',db.String(45))
    start_org_name = db.Column('start_org_name',db.String(100))
    transfer_center_set = db.Column('transfer_center_set',db.String(1000))
    end_org_code = db.Column('end_org_code',db.String(45))
    end_org_name = db.Column('end_org_name',db.String(100))
    line_frequency_no = db.Column('line_frequency_no',db.String(45))
    line_frequency_name = db.Column('line_frequency_name',db.String(100))
    start_time = db.Column('start_time',db.TIMESTAMP)
    end_time = db.Column('end_time',db.TIMESTAMP)
    trans_type = db.Column('trans_type',db.String(12))
    line_property = db.Column('line_property',db.String(12))
    day_span = db.Column('day_span',db.Integer)
    status = db.Column('status',db.Integer)
    full_take_time = db.Column('full_take_time',db.String(100))
    full_distance = db.Column('full_distance',db.String(100))
    line_status = db.Column('line_status',db.Integer)
    fre_status = db.Column('fre_status',db.String(45))
    create_time = db.Column('create_time',db.TIMESTAMP,default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP)
    

    def __init__(self,line_no,line_name,start_org_code,start_org_name,transfer_center_set,end_org_code,end_org_name,line_frequency_no,line_frequency_name,start_time,end_time,day_span,full_take_time,full_distance,line_property,trans_type,line_status,fre_status,status=0):
        self.line_no = line_no
        self.line_name = line_name
        self.start_org_code = start_org_code
        self.start_org_name = start_org_name
        self.transfer_center_set = transfer_center_set
        self.end_org_code = end_org_code
        self.end_org_name = end_org_name
        self.line_frequency_no = line_frequency_no
        self.line_frequency_name = line_frequency_name
        self.start_time = start_time
        self.end_time = end_time
        self.day_span = day_span
        self.full_take_time = full_take_time
        self.full_distance = full_distance
        self.line_property = line_property
        self.trans_type = trans_type
        self.line_status = line_status
        self.fre_status = fre_status
        self.status = status
        self.create_time = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
