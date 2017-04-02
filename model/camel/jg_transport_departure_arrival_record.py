#-*- coding:utf-8 -*-
__author__ = "Zc"
__date__ = "2016-04-08"

import sys
import hashlib
import datetime
from instance.camel_app import db

class JG_Transport_Departure_Arrival_Record(db.Model):
    """
    jg_createTime,uploadTime,uploadDate data type should datetime or timestamp,not varchar.

    """
    __tablename__ = 'JG_Transport_Departure_Arrival_Record'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    orgCode = db.Column(db.String(45))
    opCode = db.Column(db.String(3))
    waybillNo = db.Column(db.String(24))
    vehiclePlateNo = db.Column(db.String(8))
    lineNo = db.Column(db.String(100))
    linefrequencyNo = db.Column(db.String(100))
    creat_time = db.Column(db.TIMESTAMP)
    jg_createTime = db.Column(db.TIMESTAMP)
    uploadTime = db.Column(db.TIMESTAMP)
    uploadDate = db.Column(db.String(19))
    # TODO Because of 11-11,remove fk_trans_number field.In next new version departure arrival match cq number job,add the field.
    #fk_trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))

    def __init__(self,orgCode,opCode,waybillNo,vehiclePlateNo,lineNo,linefrequencyNo,jg_createTime,uploadTime):
        self.orgCode = orgCode
        self.opCode = opCode
        self.waybillNo = waybillNo
        self.vehiclePlateNo = vehiclePlateNo
        self.lineNo = lineNo
        self.linefrequencyNo = linefrequencyNo
        self.jg_createTime = jg_createTime
        self.uploadTime = uploadTime
        self.uploadDate = jg_createTime[:10]

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
