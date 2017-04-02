#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-04-08"

import sys
import hashlib
import datetime
from instance.camel_app import db

class JG_TDAR_Record(db.Model):
    __tablename__ = 'JG_TDAR_Record'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    orgCode = db.Column(db.String(45))
    opCode = db.Column(db.String(3))
    waybillNo = db.Column(db.String(24))
    vehiclePlateNo = db.Column(db.String(8))
    lineNo = db.Column(db.String(100))
    linefrequencyNo = db.Column(db.String(100))
    camel_create_time = db.Column(db.TIMESTAMP)
    jg_createTime = db.Column(db.String(19))
    uploadTime = db.Column(db.String(19))
    create_at = db.Column(db.TIMESTAMP)

    def __init__(self,orgCode,opCode,waybillNo,vehiclePlateNo,lineNo,linefrequencyNo,camel_create_time,jg_createTime,uploadTime):
        self.orgCode = orgCode
        self.opCode = opCode
        self.waybillNo = waybillNo
        self.vehiclePlateNo = vehiclePlateNo
        self.lineNo = lineNo
        self.linefrequencyNo = linefrequencyNo
        self.camel_create_time = camel_create_time
        self.jg_createTime = jg_createTime
        self.uploadTime = uploadTime

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
