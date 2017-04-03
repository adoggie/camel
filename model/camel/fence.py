#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-29"

import sys
import hashlib
import datetime

from camel.biz.application.flasksrv import db

class Fence(db.Model):
    __tablename__ = "Fence"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    fence_id = db.Column(db.String(256),index=True,unique=True)
    fence_name = db.Column(db.String(256))
    radius = db.Column(db.Integer)
    th_trigger_at = db.Column(db.TIMESTAMP)
    create_at = db.Column(db.TIMESTAMP)
    trigger_at = db.Column(db.TIMESTAMP,default = datetime.datetime.now())
    status = db.Column(db.Integer)
    fk_trans_number = db.Column(db.String(24))
    fk_location_code = db.Column(db.String(7))

    def __init__(self,fence_id,fence_name,radius,create_at,th_trigger_at,trigger_at,status,fk_trans_number,fk_location_code):
        self.fence_id = fence_id
        self.fence_name = fence_name
        self.radius = radius
        self.create_at = create_at
        self.th_trigger_at = th_trigger_at
        self.trigger_at = trigger_at
        self.status = status    # 1:已创建 2:已出发
        self.fk_trans_number = fk_trans_number
        self.fk_location_code = fk_location_code
        self.create_at = datetime.datetime.now() 

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
