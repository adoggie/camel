#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.user import User
from model.address import Address
from model.cargo import Cargo

class Logistics_Bill_Desc(db.Model):
    __tablename__ = 'Logistics_Bill_Desc'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    bill_number = db.Column(db.String(24),nullable=False,index = True,unique=True)
    consignor_name = db.Column(db.String(24))
    consignor_email = db.Column(db.String(24))
    consignor_phone = db.Column(db.String(15))
    consignor_mobile = db.Column(db.String(15))
    at_address = db.Column(db.TEXT)
    consignee_name = db.Column(db.String(24))
    consignee_email = db.Column(db.String(24))
    consignee_phone = db.Column(db.String(15))
    consignee_mobile = db.Column(db.String(15))
    to_address = db.Column(db.TEXT)
    at_date = db.Column(db.Date)
    at_segment_type = db.Column(db.Integer)
    to_date = db.Column(db.Date)
    to_segment_type = db.Column(db.Integer)
    delivery_type = db.Column(db.Integer)
    note = db.Column(db.TEXT)
    is_receipt = db.Column(db.BOOLEAN)
    receipt_count = db.Column(db.Integer)
    receipt_number = db.Column(db.Integer)
    total_account = db.Column(db.FLOAT)
    xf_account = db.Column(db.FLOAT)
    df_account = db.Column(db.FLOAT)
    hdf_account = db.Column(db.FLOAT)
    yj_account = db.Column(db.FLOAT)
    dianf_account = db.Column(db.FLOAT)
    cargo_total_weight = db.Column(db.FLOAT)
    cargo_total_volumn = db.Column(db.FLOAT)
    create_date = db.Column(db.Date,default =datetime.datetime.now())
    create_time = db.Column(db.TIMESTAMP,default = datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP,default = datetime.datetime.now())
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    fk_trans_number = db.Column(db.String(24),db.ForeignKey("Transport_Protocol.trans_number"))
    fk_at_address_id = db.Column(db.Integer,db.ForeignKey("Address.id"))
    fk_to_address_id = db.Column(db.Integer,db.ForeignKey("Address.id"))
    operator = db.relationship('User',backref='Logistics_Bill_Desc',uselist=False,foreign_keys=[fk_operator_id])
    o_at_address = db.relationship('Address',uselist=False,foreign_keys=[fk_at_address_id])
    o_to_address = db.relationship('Address',uselist=False,foreign_keys=[fk_to_address_id])
    cargos = db.relationship('Cargo')
    

    def __init__(self,bill_number,consignor_name,consignor_email,consignor_phone,consignor_mobile,at_address,consignee_name,consignee_email,consignee_phone,consignee_mobile,to_address,at_date,at_segment_type,to_date,to_segment_type,delivery_type,note,is_receipt,receipt_count,receipt_number,xf_account,df_account,hdf_account,yj_account,update_time,fk_operator_id,fk_trans_number,o_at_address,o_to_address,dianf_account,cargo_total_weight,cargo_total_volumn):
        self.bill_number = bill_number
        self.consignor_name = consignor_name
        self.consignor_email = consignor_email
        self.consignor_phone = consignor_phone
        self.consignor_mobile = consignor_mobile
        self.at_address = at_address
        self.consignee_name = consignee_name
        self.consignee_email = consignee_email
        self.consignee_phone = consignee_phone
        self.consignee_mobile = consignee_mobile
        self.to_address = to_address
        self.at_date = at_date
        self.at_segment_type = at_segment_type
        self.to_date = to_date
        self.to_segment_type = to_segment_type
        self.delivery_type = delivery_type
        self.note = note
        self.is_receipt = is_receipt
        self.receipt_count = receipt_count
        self.receipt_number = receipt_number
        self.xf_account = xf_account
        self.df_account = df_account
        self.hdf_account = hdf_account
        self.yj_account = yj_account
        if update_time:
            self.update_time = update_time
        else:
            self.update_time = datetime.datetime.now()
        self.fk_operator_id = fk_operator_id
        self.fk_trans_number = fk_trans_number
        self.o_at_address = o_at_address
        self.o_to_address = o_to_address
        self.dianf_account = dianf_account
        self.cargo_total_weight = cargo_total_weight
        self.cargo_total_volumn = cargo_total_volumn
        self.create_date = datetime.datetime.now()
        self.create_time = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
