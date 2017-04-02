#-*- coding:utf-8 -*-
__author__ = "Yzk"
__date__ ="$2016-10-18"

import sys
from instance.camel_app import db

class Dashboard_Data(db.Model):
    __tablename__ = 'Dashboard_Data'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    trans_number = db.Column('trans_number',db.String(15))
    line_name = db.Column('line_name',db.String(1000))
    full_take_time = db.Column('full_take_time',db.String(100))
    start_code = db.Column('start_code',db.String(6))
    end_code = db.Column('end_code',db.String(6))
    plate = db.Column(db.String(8))
    volume = db.Column(db.FLOAT)
    run_mode = db.Column(db.Integer)    # 0.单边车 1.双边车
    vehicle_type = db.Column(db.String(45))
    carrier_name = db.Column(db.String(512))
    report_type = db.Column('report_type',db.Integer)
    create_time = db.Column('create_time',db.TIMESTAMP)
    startoff_time = db.Column('startoff_time',db.TIMESTAMP)
    on_way_time = db.Column('on_way_time',db.TIMESTAMP)
    complete_time = db.Column('complete_time',db.TIMESTAMP)
    unusual_time = db.Column('unusual_time',db.TIMESTAMP)
    abolish_time = db.Column('abolish_time',db.TIMESTAMP)
    jg_fc_time = db.Column('jg_fc_time',db.TIMESTAMP)
    jg_jc_time = db.Column('jg_jc_time',db.TIMESTAMP)
    trans_status = db.Column('trans_status',db.Integer)
    jg_status = db.Column('jg_status',db.Integer)
    expect_time = db.Column('expect_time',db.TIMESTAMP)

    def __init__(self, trans_number, line_name, full_take_time, start_code, end_code,
                plate, volume, run_mode, vehicle_type, carrier_name, report_type,
                create_time, startoff_time, on_way_time, complete_time, unusual_time,
                abolish_time, jg_fc_time, jg_jc_time, trans_status, jg_status, expect_time):
        self.trans_number = trans_number
        self.line_name = line_name
        self.full_take_time = full_take_time
        self.start_code = start_code
        self.end_code = end_code
        self.plate = plate
        self.volume = volume
        self.run_mode = run_mode
        self.vehicle_type = vehicle_type
        self.carrier_name = carrier_name
        self.report_type = report_type
        self.create_time = create_time
        self.startoff_time = startoff_time
        self.on_way_time = on_way_time
        self.complete_time = complete_time
        self.unusual_time = unusual_time
        self.abolish_time = abolish_time
        self.jg_fc_time = jg_fc_time
        self.jg_jc_time = jg_jc_time
        self.trans_status = trans_status
        self.jg_status = jg_status
        self.expect_time = expect_time

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
