#-*- coding:utf-8 -*-
__author__ = "bo"
__date__ = "2016-01-27"

import sys
import hashlib
import datetime
from instance.camel_app import db
from model.logistics_bill_desc import Logistics_Bill_Desc
from model.notify_his import Notify_His
from model.transport_protocol_flow import Transport_Protocol_Flow
from model.driver_live_reporting import Driver_Live_Reporting
from model.driver import Driver
from model.transport_location import Transport_Location
from model.user import User
from model.truck import Truck
from model.line import Line
from model.rs_cq_trans import RS_CQ_Trans
from model.transport_protocol_relay import Transport_Protocol_Relay

class Transport_Protocol(db.Model):
    __tablename__ = 'Transport_Protocol'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    trans_number = db.Column('trans_number',db.String(15))
    start_time = db.Column('start_time',db.String(16))
    end_time = db.Column('end_time',db.String(16))
    settlement_mode = db.Column('settlement_mode',db.String(4))
    driver_freight = db.Column('driver_freight',db.FLOAT)
    plate = db.Column(db.String(8))
    create_date = db.Column(db.Date,default=datetime.date.today())
    create_time = db.Column(db.TIMESTAMP,default=datetime.datetime.now())
    status = db.Column('status',db.Integer)
    status_time = db.Column(db.TIMESTAMP,default=datetime.datetime.now())
    update_time = db.Column('update_time',db.TIMESTAMP,default=datetime.datetime.now())
    is_onway = db.Column('is_onway',db.Integer)
    is_temp_truck = db.Column('is_temp_truck',db.Integer)
    is_overtime = db.Column('is_overtime',db.Integer)
    fk_driver_id = db.Column('fk_driver_id',db.Integer,db.ForeignKey("Driver.id"))
    fk_to_location_code = db.Column(db.String(6),db.ForeignKey("Transport_Location.code"))
    fk_at_location_code = db.Column(db.String(6),db.ForeignKey("Transport_Location.code"))
    fk_operator_id = db.Column(db.Integer,db.ForeignKey("User.id"))
    line_no = db.Column(db.String(256),db.ForeignKey("Line.line_no"))
    fk_truck_id = db.Column(db.Integer,db.ForeignKey("Truck.id"))
    relay_status = db.Column(db.Integer)
    carrier_name = db.Column(db.String(512))
    vehicle_type = db.Column(db.String(45)) # 车辆长度 17.9米
    run_mode = db.Column(db.Integer) # 0:单边车 1:双边车
    is_link = db.Column(db.Integer)
    link = db.Column('link',db.String(15))
    voucher = db.Column('voucher',db.String(64))
    
    logsitics_bills = db.relationship('Logistics_Bill_Desc',backref="Transport_Protocol",lazy='dynamic')
    Notifys = db.relationship('Notify_His',backref="Transport_Protocol",lazy='dynamic')
    status_flows = db.relationship("Transport_Protocol_Flow",backref="Transport_Protocol",lazy="dynamic")
    live_reportings = db.relationship("Driver_Live_Reporting",lazy="dynamic")

    driver = db.relationship("Driver",backref="Transport_Protocol",uselist=False,foreign_keys=[fk_driver_id])
    at_location = db.relationship("Transport_Location",uselist=False,foreign_keys=[fk_at_location_code])
    to_location = db.relationship("Transport_Location",uselist=False,foreign_keys=[fk_to_location_code])
    operator = db.relationship("User",uselist=False,foreign_keys=[fk_operator_id])
    line = db.relationship("Line",uselist=False,foreign_keys=[line_no])
    truck = db.relationship("Truck",uselist=False,foreign_keys=[fk_truck_id])
    rs_cq_trans = db.relationship("RS_CQ_Trans",uselist=False)
    relays = db.relationship('Transport_Protocol_Relay',lazy='dynamic')

    def __init__(self,trans_number,start_time,end_time,settlement_mode,driver_freight,plate,status,status_time,update_time,fk_driver_id,fk_to_location_code,fk_at_location_code,fk_operator_id,relay_status,is_onway,is_temp_truck,is_overtime,line_no,carrier_name,is_link,vehicle_type,run_mode,voucher,fk_truck_id):
        self.trans_number = trans_number
        self.start_time = start_time
        self.end_time = end_time
        self.settlement_mode = settlement_mode
        self.driver_freight = driver_freight
        self.plate = plate
        self.status = status
        self.status_time = status_time
        if update_time:
            self.update_time = update_time
        else:
            self.update_time = datetime.datetime.now()
        self.fk_driver_id = fk_driver_id
        self.fk_to_location_code = fk_to_location_code
        self.fk_at_location_code = fk_at_location_code
        self.fk_operator_id = fk_operator_id
        self.create_date = datetime.datetime.now()
        self.create_time = datetime.datetime.now()
        self.relay_status = relay_status
        self.is_onway = is_onway
        self.is_temp_truck = is_temp_truck
        self.is_overtime = is_overtime
        self.line_no = line_no
        self.carrier_name = carrier_name
        self.is_link = is_link
        self.vehicle_type = vehicle_type
        self.run_mode = run_mode
        self.voucher = voucher
        self.fk_truck_id = fk_truck_id
    
    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict: 
            del dict['_sa_instance_state']
        return dict 

    @property 
    def relay_index(self):
        if self.relay_status:
            return self.relay_status/10
        else:
            return 0

    @property 
    def relay_type(self):
        return self.relay_status - (self.relay_status/10)*10

    def relay_locations(self):
        _relay = self.relays
        if not _relay:
            return []
        else:
            i = 1
            locs = []
            sort_relay = sorted(_relay,key=lambda relay : relay.index) 
            for item in sort_relay:
                loc_dict = item.to_dict()
                loc_dict = dict(loc_dict,**item.location.to_dict())
                loc_dict['relay_status'] = 0
                if i< int(self.relay_index):
                    loc_dict['relay_status'] = 2#出发
                elif i== int(self.relay_index):
                    loc_dict['relay_status'] = self.relay_type
                locs.append(loc_dict)
                i+=1
            return locs  
