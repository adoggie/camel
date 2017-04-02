#-*- coding:utf-8 -*-
__author__ = "Yzk"
__date__ = "2016-12-02"

import sys
import datetime
from instance.camel_app import db

class T_MOT_UNIT_VEHICLE_OWNER(db.Model):
    __tablename__ = 'T_MOT_UNIT_VEHICLE_OWNER'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    vehicle_owner_id = db.Column('vehicle_owner_id',db.String(100))
    company_name = db.Column('company_name',db.String(100))
    company_address = db.Column('company_address',db.String(1000))
    contact_number = db.Column('contact_number',db.String(20))
    fax_no = db.Column('fax_no',db.String(20))
    version_no = db.Column('version_no',db.Integer)
    unit_vehicle_owner_no = db.Column('unit_vehicle_owner_no',db.String(100))
    vehicle_owned_company = db.Column('vehicle_owned_company',db.String(100))
    company_code = db.Column('company_code',db.String(7))
    owned_company_name = db.Column('owned_company_name',db.String(100))
    jg_modify_at = db.Column('jg_modify_at',db.TIMESTAMP)
    create_at = db.Column('create_at',db.TIMESTAMP)

    def __init__(self,vehicle_owner_id,company_name,company_address,contact_number,
            fax_no,version_no,unit_vehicle_owner_no,vehicle_owned_company,company_code,
            owned_company_name,jg_modify_at):
        self.vehicle_owner_id = vehicle_owner_id
        self.company_name = company_name
        self.company_address = company_address
        self.contact_number = contact_number
        self.fax_no = fax_no
        self.version_no = version_no
        self.unit_vehicle_owner_no = unit_vehicle_owner_no
        self.vehicle_owned_company = vehicle_owned_company
        self.company_code = company_code
        self.owned_company_name = owned_company_name
        self.jg_modify_at = jg_modify_at
        self.create_at = datetime.datetime.now()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 
