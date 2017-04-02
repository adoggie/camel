#-*- coding:utf-8 -*-
__author__ = "Yzk"
__date__ = "2016-12-02"

import sys
import datetime
from instance.camel_app import db

class T_MOT_VEHICLE_OWNER(db.Model):
    __taledname__ = 'T_MOT_VEHICLE_OWNER'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    vehicle_owner_id = db.Column('vehicle_owner_id',db.String(100),nullable=False)
    man_in_charge_name = db.Column('man_in_charge_name',db.String(100))
    man_in_charge_phone_number = db.Column('man_in_charge_phone_number',db.String(30))
    bank_card_no = db.Column('bank_card_no',db.String(20))
    account_bank = db.Column('account_bank',db.String(100))
    bank_card_name = db.Column('bank_card_name',db.String(20))
    emergency_contact_name = db.Column('emergency_contact_name',db.String(100))
    emergency_contact_phone_number = db.Column('emergency_contact_phone_number',db.String(20))
    vehicle_owner_type = db.Column('vehicle_owner_type',db.Integer)
    status = db.Column('status',db.String(20))
    version_no = db.Column('version_no',db.Integer)
    residential_address = db.Column('residential_address',db.String(1000))
    residential_phone_number = db.Column('residential_phone_number',db.String(20))
    vehicle_owner_no = db.Column('vehicle_owner_no',db.String(100))
    identity_card_address = db.Column('identity_card_address',db.String(100))
    org_name = db.Column('org_name',db.String(100))
    org_code = db.Column('org_code',db.String(100))
    general_taxpayer_flag = db.Column('general_taxpayer_flag',db.String(4))
    rate = db.Column('rate',db.Float)
    registration_number = db.Column('registration_number',db.String(32))
    organization_code = db.Column('organization_code',db.String(20))
    tax_registration_no = db.Column('tax_registration_no',db.String(20))
    registered_captital = db.Column('registered_captital',db.String(100))
    vehicle_owned_company = db.Column('vehicle_owned_company',db.String(100))
    owned_company_name = db.Column('owned_company_name',db.String(100))
    approve_status = db.Column('approve_status',db.Integer)
    execution_date = db.Column('execution_date',db.Date)
    jg_modify_at = db.Column('jg_modify_at',db.TIMESTAMP)
    create_at = db.Column('create_at',db.TIMESTAMP)

    def __init__(self,vehicle_owner_id,man_in_charge_name,man_in_charge_phone_number,
            bank_card_no,account_bank,bank_card_name,emergency_contact_name,
            emergency_contact_phone_number,vehicle_owner_type,status,version_no,
            residential_address,residential_phone_number,vehicle_owner_no,identity_card_address,
            org_name,org_code,general_taxpayer_flag,rate,registration_number,organization_code,
            tax_registration_no,registered_captital,vehicle_owned_company,owned_company_name,
            approve_status,execution_date,jg_modify_at):
        self.vehicle_owner_id = vehicle_owner_id
        self.man_in_charge_name = man_in_charge_name
        self.man_in_charge_phone_number = man_in_charge_phone_number
        self.bank_card_no = bank_card_no
        self.account_bank = account_bank
        self.bank_card_name = bank_card_name
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone_number = emergency_contact_phone_number
        self.vehicle_owner_type = vehicle_owner_type
        self.status = status
        self.version_no = version_no
        self.residential_address = residential_address
        self.residential_phone_number = residential_phone_number
        self.vehicle_owner_no = vehicle_owner_no
        self.identity_card_address = identity_card_address
        self.org_name = org_name
        self.org_code = org_code
        self.general_taxpayer_flag = general_taxpayer_flag
        self.rate = rate
        self.registration_number = registration_number
        self.organization_code = organization_code
        self.tax_registration_no = tax_registration_no
        self.registered_captital = registered_captital
        self.vehicle_owned_company = vehicle_owned_company
        self.owned_company_name = owned_company_name
        self.approve_status = approve_status
        self.execution_date = execution_date
        self.jg_modify_at = jg_modify_at
        self.create_at = datetime.datetime.now()
    
    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 

