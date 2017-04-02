#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.transport_protocol import Transport_Protocol
from model.user import User

class Transport_Protocol_Note(db.Model):
    __tablename__ = 'Transport_Protocol_Note'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    note = db.Column('note',db.TEXT)
    note_type = db.Column('note_type',db.Integer)
    fk_trans_number = db.Column(db.String(15),db.ForeignKey("Transport_Protocol.trans_number"))
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    upload_time = db.Column('upload_time',db.TIMESTAMP)
    #create_time = db.Column(db.TIMESTAMP,default=datetime.datetime.now())
    create_time = db.Column(db.TIMESTAMP)
    location_code = db.Column(db.String(6))
    line_no = db.Column(db.String(100))

    operator = db.relationship("User",uselist=False,foreign_keys=[fk_operator_id])

    def __init__(self,note,note_type,fk_trans_number,fk_operator_id,upload_time=datetime.datetime.now()):
        self.note = note
        self.note_type = note_type
        self.fk_trans_number = fk_trans_number
        self.fk_operator_id = fk_operator_id
        self.upload_time = upload_time

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
