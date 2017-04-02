# ! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
Model module for yto.camel's CYS system.
'''

# History
# -------
#
# George Gao started this module.  A Kun  changed the
# Truck class and the api document.  The multipart
# parsing was inspired by code submitted by Gao. ZhouTing
# tested it, George Gao reformatted and documented the module and is currently
# responsible for its maintenance.
#

__version__ = '0.1'
__author__ = 'GYZ'
__date__ = '2016-04-21'


# Imports
# =======

from . import db
import time
import json
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import text
from sqlalchemy.dialects.mysql import TINYINT
import datetime


# Classes for field storage
# =========================
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    email = db.Column('email',db.String(50),index=True,unique=True,nullable=False)
    password = db.Column('password',db.String(256),nullable=False)
    com_name = db.Column('com_name',db.String(30),nullable=False)
    com_type = db.Column('com_type',db.Integer,nullable=False,default=0)
    passwd_expire = db.Column('passwd_expire',db.Boolean,default=0)
    # :0 means company, 1 means person
    address = db.Column('address',db.String(128))
    role = db.Column('role',db.Integer,nullable=False,default=0)
    # :0 means normal user, 1 means yto inner users

    # shipper = db.relationship('Shipper',backref='user',lazy='select',uselist=False)

    def __repr__(self):
        return '<User email %r>' % self.email

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict


class Shipper(db.Model):
    __tablename__ = 'shippers'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    com_name = db.Column('com_name',db.String(30),nullable=False)
    com_about = db.Column('com_about',db.String(200),nullable=False)
    better_area = db.Column('better_area',db.String(256),nullable=False)
    buss_id = db.Column('buss_id',db.String(20),nullable=False)
    url_buss_id = db.Column('url_buss_id', db.String(128))
    buss_money  = db.Column('buss_money',db.String(20),nullable=False)
    entp_id = db.Column('entp_id',db.String(20),nullable=False)
    url_entp_id = db.Column('url_entp_id', db.String(128))
    trans_id = db.Column('trans_id',db.String(20),nullable=False)
    url_trans_id = db.Column('url_trans_id', db.String(128))
    url_insurance = db.Column('url_insurance', db.String(128))
    legalp_name = db.Column('legalp_name',db.String(20),nullable=False)
    legalp_home = db.Column('legalp_home',db.String(20),nullable=False)
    legalp_cid = db.Column('legalp_cid',db.String(18),nullable=False)
    legalp_phone = db.Column('legalp_phone',db.String(25),nullable=False)
    legalp_email = db.Column('legalp_email',db.String(50),nullable=False)
    url_fcid = db.Column('url_fcid', db.String(128),nullable=False)
    url_bcid = db.Column('url_bcid', db.String(128),nullable=False)
    tax_id = db.Column('tax_id',db.String(20),nullable=False)
    url_tax = db.Column('url_tax', db.String(128))
    b_account = db.Column('b_account',db.String(30),nullable=False)
    b_com = db.Column('b_com',db.String(30),nullable=False)
    b_bank = db.Column('b_bank',db.String(30),nullable=False)
    url_b_passport = db.Column('url_b_passport', db.String(128))
    url_b_taxer = db.Column('url_b_taxer', db.String(128))
    url_profit = db.Column('url_profit', db.String(128))
    url_audit_report = db.Column('url_audit_report', db.String(128))
    url_addtax = db.Column('url_addtax', db.String(128))
    url_property = db.Column('url_property', db.String(128))
    contact_name = db.Column('contact_name',db.String(20),nullable=False)
    contact_cid = db.Column('contact_cid',db.String(18),nullable=False)
    contact_home = db.Column('contact_home',db.String(20),nullable=False)
    contact_phone = db.Column('contact_phone',db.String(25),nullable=False)
    contact_email = db.Column('contact_email',db.String(50),nullable=False)
    contact_postion = db.Column('contact_postion',db.String(20),nullable=False)
    contact_depart = db.Column('contact_depart',db.String(20),nullable=False)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    status = db.Column('status',db.Integer,nullable=False,default=0)
    # status 0 is empty, 1 is tmp save, 2 is commit
    user_id = db.Column('user_id',db.Integer)

    # truck = db.relationship('Truck',backref='shipper',lazy='select')
    # commit = db.relationship('Commit',backref='shipper',lazy='select',uselist=False)
    # commit_his = db.relationship('Commit_his',backref='shipper',lazy='select')

    def __repr__(self):
        return '<Shipper com_name %r>' % self.com_name

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            dict['create_time'] = dict['create_time'].strftime("%Y-%m-%d %H:%M:%S")
        if 'id' in dict:
            del dict['id']
        return dict


class Truck(db.Model):
    __tablename__ = 'trucks'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    plate = db.Column('plate', db.String(7), index=True)
    vehicle_type = db.Column('vehicle_type', db.String(25))
    brand = db.Column('brand', db.String(25))
    vehicle_model = db.Column('vehicle_model', db.String(25))
    engine_model = db.Column('engine_model', db.String(25))
    power = db.Column('power', db.Float)
    horsepower = db.Column('horsepower', db.Float)
    vin = db.Column('vin', db.String(20))
    truck_length = db.Column('truck_length', db.Float)
    truck_width = db.Column('truck_width', db.Float)
    truck_height = db.Column('truck_height', db.Float)
    carriage_length = db.Column('carriage_length', db.Float)
    carriage_width = db.Column('carriage_width', db.Float)
    carriage_height = db.Column('carriage_height', db.Float)
    carriage_type = db.Column('carriage_type', TINYINT())
    volume = db.Column('volume', db.Float)
    total_mass = db.Column('total_mass', db.Float)
    equipment_mass = db.Column('equipment_mass', db.Float)
    limit_mass = db.Column('limit_mass', db.Float)
    limit_person = db.Column('limit_person', db.Integer)
    belong_to = db.Column('belong_to', db.String(25))
    purchase_at = db.Column('purchase_at', db.Date)
    abolish_at = db.Column('abolish_at', db.Date)
    vehicle_license_no = db.Column('vehicle_license_no', db.Integer)
    voc_no = db.Column('voc_no', db.String(25))
    insurance_from = db.Column('insurance_from', db.Date)
    insurance_end = db.Column('insurance_end', db.Date)
    insurance_com = db.Column('insurance_com', db.String(25))
    insurance_amount = db.Column('insurance_amount', db.Float)
    url_vehicle_license = db.Column('url_vehicle_license', db.String(512))
    url_voc = db.Column('url_voc', db.String(512))
    url_vrc = db.Column('url_vrc', db.String(512))
    url_truck_jqx = db.Column('url_truck_jqx', db.String(512))
    url_truck_syx = db.Column('url_truck_syx', db.String(512))
    truck_type = db.Column('truck_type', TINYINT())
    # truck_status = db.Column('truck_status', TINYINT())
    shipper_id = db.Column('shipper_id', db.Integer)
    commit_status = db.Column('commit_status', db.Integer, nullable=False,default=0)
    committer  = db.Column('committer', db.String(30))
    # 0 have no commit, 1: committed ok
    create_at = db.Column('create_at', db.TIMESTAMP)
    update_at = db.Column('update_at', db.TIMESTAMP)




    def __init__(self, plate, vehicle_type, brand, vehicle_model, engine_model,
                 power, horsepower, vin, truck_length, truck_width, truck_height,
                 carriage_length, carriage_width, carriage_height, carriage_type, volume,
                 total_mass, equipment_mass, limit_mass, limit_person, belong_to,
                 purchase_at, abolish_at, vehicle_license_no, voc_no, insurance_from,
                 insurance_end, insurance_com, insurance_amount, url_vehicle_license,
                 url_voc, url_vrc, url_truck_jqx, url_truck_syx, truck_type, shipper_id):
        self.plate = plate
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.vehicle_model = vehicle_model
        self.engine_model = engine_model
        self.power = power
        self.horsepower = horsepower
        self.vin = vin
        self.truck_length = truck_length
        self.truck_width = truck_width
        self.truck_height = truck_height
        self.carriage_length = carriage_length
        self.carriage_width = carriage_width
        self.carriage_height = carriage_height
        self.carriage_type = carriage_type
        self.volume = volume
        self.total_mass = total_mass
        self.equipment_mass = equipment_mass
        self.limit_mass = limit_mass
        self.limit_person = limit_person
        self.belong_to = belong_to
        self.purchase_at = purchase_at
        self.abolish_at = abolish_at
        self.vehicle_license_no = vehicle_license_no
        self.voc_no = voc_no
        self.insurance_from = insurance_from
        self.insurance_end = insurance_end
        self.insurance_com = insurance_com
        self.insurance_amount = insurance_amount
        self.url_vehicle_license = url_vehicle_license
        self.url_voc = url_voc
        self.url_vrc = url_vrc
        self.url_truck_jqx = url_truck_jqx
        self.url_truck_syx = url_truck_syx
        self.truck_type = truck_type
        # self.truck_status = truck_status
        self.create_at = datetime.datetime.now()
        self.shipper_id = shipper_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        if 'purchase_at' in dict and dict['purchase_at'] is not None:
            dict['purchase_at'] = datetime.datetime.strftime(dict['purchase_at'], '%Y-%m-%d')
        if 'abolish_at' in dict and dict['abolish_at'] is not None:
            dict['abolish_at'] = datetime.datetime.strftime(dict['abolish_at'], '%Y-%m-%d')
        if 'insurance_from' in dict and dict['insurance_from'] is not None:
            dict['insurance_from'] = datetime.datetime.strftime(dict['insurance_from'], '%Y-%m-%d')
        if 'insurance_end' in dict and dict['insurance_end'] is not None:
            dict['insurance_end'] = datetime.datetime.strftime(dict['insurance_end'], '%Y-%m-%d')
        if 'create_at' in dict and dict['create_at']:
            dict['create_at'] = datetime.datetime.strftime(dict['create_at'], "%Y-%m-%d %H:%M:%S")
        if 'vehicle_type' in dict and not dict['vehicle_type']:
            dict['vehicle_type'] = ''
        if 'brand' in dict and not dict['brand']:
            dict['brand'] = ''
        if 'vehicle_model' in dict and not dict['vehicle_model']:
            dict['vehicle_model'] = ''
        if 'engine_model' in dict and not dict['engine_model'] :
            dict['engine_model'] = ''

        if 'power' in dict and not dict['power'] :
            dict['power'] = ''

        if 'horsepower' in dict and not dict['horsepower']:
            dict['horsepower'] = ''

        if 'vin' in dict and not not dict['vin'] :
            dict['vin'] = ''

        if 'truck_length' in dict and not dict['truck_length']:
            dict['truck_length'] = ''

        if 'truck_width' in dict and not dict['truck_width']:
            dict['truck_width'] = ''

        if 'truck_height' in dict and not dict['truck_height'] :
            dict['truck_height'] = ''

        if 'carriage_length' in dict and not dict['carriage_length'] :
            dict['carriage_length'] = ''

        if 'carriage_type' in dict and not dict['carriage_type'] :
            dict['carriage_type'] = ''

        if 'volume' in dict and not dict['volume'] :
            dict['volume'] = ''

        if 'total_mass' in dict and not dict['total_mass'] :
            dict['total_mass'] = ''

        if 'equipment_mass' in dict and not dict['equipment_mass']:
            dict['equipment_mass'] = ''

        if 'limit_mass' in dict and not dict['limit_mass'] :
            dict['limit_mass'] = ''

        if 'limit_person' in dict and not dict['limit_person']:
            dict['limit_person'] = ''

        if 'belong_to' in dict and not dict['belong_to'] :
            dict['belong_to'] = ''

        if 'purchase_at' in dict and not dict['purchase_at']:
            dict['purchase_at'] = ''

        if 'abolish_at' in dict and not dict['abolish_at'] :
            dict['abolish_at'] = ''

        if 'vehicle_license_no' in dict and not dict['vehicle_license_no'] :
            dict['vehicle_license_no'] = ''

        if 'voc_no' in dict and not dict['voc_no'] :
            dict['voc_no'] = ''

        if 'insurance_from' in dict and not dict['insurance_from']:
            dict['insurance_from'] = ''

        if 'insurance_end' in dict and not dict['insurance_end'] :
            dict['insurance_end'] = ''

        if 'insurance_com' in dict and not dict['insurance_com'] :
            dict['insurance_com'] = ''

        if 'insurance_amount' in dict and not dict['insurance_amount'] :
            dict['insurance_amount'] = ''

        if 'url_vehicle_license' in dict and not dict['url_vehicle_license'] :
            dict['url_vehicle_license'] = ''

        if 'url_voc' in dict and not dict['url_voc']:
            dict['url_voc'] = ''

        if 'url_vrc' in dict and not dict['url_vrc']:
            dict['url_vrc'] = ''

        if 'url_truck_jqx' in dict and not dict['url_truck_jqx']:
            dict['url_truck_jqx'] = ''

        if 'url_truck_syx' in dict and not dict['url_truck_syx']:
            dict['url_truck_syx'] = ''

        if 'truck_type' in dict and not dict['truck_type']:
            dict['truck_type'] = ''
        return dict

# class Truck(db.Model):
#     __tablename__ = 'trucks'
#
#     id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
#     plate = db.Column('plate',db.String(7),index=True,nullable=False)
#     brand = db.Column('brand',db.Integer,nullable=False)
#     truck_type = db.Column('type',db.Boolean,nullable=False)
#     power = db.Column(db.Float,nullable=False)
#     length = db.Column(db.Integer,nullable=False)
#     volume = db.Column(db.Float,nullable=False)
#     flic_date = db.Column('flic_date',db.Date,nullable=False)
#     blic_date = db.Column('blic_date',db.Date,nullable=True)
#     insurance_from = db.Column('insurance_from',db.Date,nullable=False)
#     insurance_end = db.Column('insurance_end',db.Date,nullable=False)
#     insurance_com = db.Column('insurance_com',db.String(128),nullable=False)
#     insurance_amount = db.Column('insurance_amount',db.Integer,nullable=False)
#     line_type = db.Column('line_type',db.String(32))
#     line = db.Column('line',db.String(128))
#     url_truck_jqx = db.Column('url_truck_jqx', db.String(128),nullable=False)
#     url_truck_lic = db.Column('url_truck_lic', db.String(128),nullable=False)
#     url_truck_yy = db.Column('url_truck_yy', db.String(128),nullable=False)
#     url_truck_dj = db.Column('url_truck_dj', db.String(128),nullable=False)
#     url_truck_syx = db.Column('url_truck_syx', db.String(128),nullable=False)
#     status = db.Column('status',db.Integer,nullable=False,default=0)
#     #0 is empty, 1 is tmp save, 2 is commit!!
#
#     shipper_id = db.Column('shipper_id',db.Integer)
#
#     def __repr__(self):
#         return '<Truck plate %r>' % self.plate
#
#     def to_dict(self):
#         dict = {}
#         dict.update(self.__dict__)
#         if '_sa_instance_state' in dict:
#             del dict['_sa_instance_state']
#         if 'id' in dict:
#             del dict['id']
#         return dict


class Commit(db.Model):
    __tablename__ = 'commits'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    reason = db.Column('reason',db.String(128),nullable=True)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    status = db.Column('status',db.Integer,nullable=False, default=0)
    #status 0 is commited, 1 is permit it, 2 is unagreed, 3 is uncomplish, 4 tmp to input truck
    star = db.Column('star',db.Boolean,nullable=False, default=0)
    temp_approved = db.Column('temp_approved',db.Integer,nullable=False, default=1)
    #star 0 is no star, 1 is staring

    shipper_id = db.Column('shipper_id',db.Integer)

    def __repr__(self):
        return '<Commit shipper_id %r>' % self.shipper_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'id' in dict:
            dict['commit_id'] = dict['id']
            del dict['id']
        if 'create_time' in dict:
            dict['commit_time'] = dict['create_time'].strftime("%Y-%m-%d %H:%M:%S")
            del dict['create_time']
        return dict


class Commit_his(db.Model):
    __tablename__ = 'commit_his'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    reason = db.Column('reason',db.String(128),nullable=True)
    status = db.Column('status',db.Integer,nullable=False)
    # time = db.Column('time',db.TIMESTAMP,default=datetime.datetime.now())
    time = db.Column('time',db.TIMESTAMP,server_default=text('now()'))
    # status 0 is commited, 1 is permit it, 2 is unagreed, 3 is uncomplish

    shipper_id = db.Column('shipper_id',db.Integer)

    def __repr__(self):
        return '<Commit_his shipper_id %r>' % self.shipper_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'id' in dict:
            del dict['id']
        if 'time' in dict:
            dict['time'] = dict['time'].strftime('%Y-%m-%d %H:%M:%S')
        return dict


class Line(db.Model):
    __tablename__ = 'line'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    line_name = db.Column('line_name',db.String(64),index=True,unique=True,nullable=False)
    run_mode = db.Column('run_mode',TINYINT(),nullable=False)
    full_distance = db.Column('full_distance',db.String(45))
    full_take_time = db.Column('full_take_time',db.String(45))
    fk_geo_id = db.Column('fk_geo_id',db.Integer,nullable=False)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))

    def __repr__(self):
        return '<Line line_name %r>' % self.line_name

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict

    def to_list(self):
        lines = [unicode(self.line_name),self.run_mode,self.full_distance,
                 self.full_take_time,self.fk_geo_id]
        print lines
        return lines


class Geo_code(db.Model):
    __tablename__ = 'geo_code'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    ad_code = db.Column('ad_code',db.Integer,nullable=False)
    ad_name = db.Column('ad_name',db.String(32),unique=True,nullable=False)
    ad_type = db.Column('ad_type',db.Integer,nullable=False,default=1)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))

    def __repr__(self):
        return '<Geo_code ad_name %r>' % self.ad_name

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict


class Truck_type(db.Model):
    __tablename__ = 'truck_type'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    length = db.Column('length',db.Integer,nullable=False)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))

    def __repr__(self):
        return '<Truck_type length %r>' % self.length

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict

    @staticmethod
    def get_truck_type(truck_length):
        """
        truck_length: truck_type's length
        """
        truck_obj = Truck_type.query.filter_by(length=int(100*(float(truck_length)))).first()
        return truck_obj


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    name = db.Column('name',db.String(128),index=True,unique=True,nullable=False)
    about = db.Column('about',db.Text,nullable=False)
    begin_time = db.Column('begin_time',db.TIMESTAMP,nullable=True)
    end_time = db.Column('end_time',db.TIMESTAMP,nullable=True)
    begin_time_01 = db.Column('begin_time_01',db.TIMESTAMP,nullable=True)
    end_time_01 = db.Column('end_time_01',db.TIMESTAMP,nullable=True)
    begin_time_02 = db.Column('begin_time_02',db.TIMESTAMP,nullable=True)
    end_time_02 = db.Column('end_time_02',db.TIMESTAMP,nullable=True)
    begin_time_03 = db.Column('begin_time_03',db.TIMESTAMP,nullable=True)
    end_time_03 = db.Column('end_time_03',db.TIMESTAMP,nullable=True)
    lines = db.Column('lines',db.Text)
    run_mode = db.Column('run_mode',TINYINT(),nullable=False)
    trucks = db.Column('trucks',db.Text)
    major_truck = db.Column('major_truck', db.Integer)
    person_in_charge_name = db.Column('person_in_charge_name',db.String(32),nullable=False)
    cid_num = db.Column('cid_num',db.String(18),nullable=False)
    contact = db.Column('contact',db.String(25),nullable=False)
    email = db.Column('email',db.String(50),nullable=False)
    bid_paper = db.Column('bid_paper',db.Text,nullable=False)
    bid_notice = db.Column('bid_notice',db.Text,nullable=False)
    status = db.Column('status',db.Integer,nullable=False, default=0)
    pub_time = db.Column('pub_time',db.TIMESTAMP,nullable=True)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))

    def __repr__(self):
        return '<Project name %r>' % self.name

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict

    def list_line(self):
        truck_obj = Truck_type.query.filter_by(id=self.major_truck).first()
        major_truck = float(truck_obj.length)/100
        dic = dict(begin_time_01=int(time.mktime(self.begin_time_01.timetuple())),
                    begin_time_02=int(time.mktime(self.begin_time_02.timetuple())),
                    begin_time_03=int(time.mktime(self.begin_time_03.timetuple())),
                    now=int(time.time()), run_mode=self.run_mode,
                    trucks=json.loads(self.trucks), major_truck=major_truck)
        return dic

    def to_list(self):
        dic = dict(id=self.id,name=self.name,about=self.about,
                   begin_time=self.begin_time,end_time=self.end_time,
                   begin_time_01=self.begin_time_01,
                   begin_time_02=self.begin_time_02,
                   begin_time_03=self.begin_time_03,
                   pub_time=self.pub_time,status=self.status)
        return dic

    def link_truck_type(self, truck_length):
        """
        truck_length: truck_type's length
        """
        truck_obj = Truck_type.get_truck_type(truck_length)
        project_truck_type = Project_truck_type(self.id, truck_obj.id)
        db.session.add(project_truck_type)

    def link_line(self, line_id):
        project_line = Project_line(self.id, line_id)
        db.session.add(project_line)


class Project_truck_type(db.Model):
    __tablename__ = 'project_truck_type'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_project_id = db.Column('fk_project_id',db.Integer,nullable=False)
    fk_truck_type_id = db.Column('fk_truck_type_id',db.Integer,nullable=False)
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    UniqueConstraint('fk_project_id', 'fk_truck_type_id')

    def __init__(self, fk_project_id, fk_truck_type_id):
        self.fk_project_id = fk_project_id
        self.fk_truck_type_id = fk_truck_type_id

    def __repr__(self):
        return '<Project_truck_type fk_project_id %r>' % self.fk_project_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict


class Project_line(db.Model):
    __tablename__ = 'project_line'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_project_id = db.Column('fk_project_id',db.ForeignKey('project.id'))
    fk_line_id = db.Column('fk_line_id',db.ForeignKey('line.id'))
    project = db.relationship("Project")
    line = db.relationship("Line")
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    UniqueConstraint('fk_project_id', 'fk_line_id')

    def __init__(self, fk_project_id, fk_line_id):
        self.fk_project_id = fk_project_id
        self.fk_line_id = fk_line_id

    def __repr__(self):
        return '<Project_line fk_project_id %r>' % self.fk_project_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict


class Shipper_project_line(db.Model):
    __tablename__ = 'shipper_project_line'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_shipper_id = db.Column('fk_shipper_id',db.ForeignKey('shippers.id'))
    fk_project_line_id = db.Column('fk_project_line_id',db.ForeignKey('project_line.id'))
    project_line = db.relationship("Project_line")
    shipper = db.relationship("Shipper")
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    UniqueConstraint('fk_shipper_id', 'fk_project_line_id')

    def __init__(self, fk_project_line_id, fk_shipper_id):
        self.fk_project_line_id = fk_project_line_id
        self.fk_shipper_id = fk_shipper_id
    def __repr__(self):
        return '<Shipper_project_line fk_shipper_id %r>' % self.fk_shipper_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict


class Bid_line_price(db.Model):
    __tablename__ = 'bid_line_price'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_shipper_project_line_id = db.Column('fk_shipper_project_line_id',db.ForeignKey('shipper_project_line.id'))
    fk_project_id = db.Column('fk_project_id',db.ForeignKey('project.id'))
    fk_line_id = db.Column('fk_line_id',db.ForeignKey('line.id'))
    fk_shipper_id = db.Column('fk_shipper_id',db.ForeignKey('shippers.id'))
    order_times = db.Column('order_times',db.Integer,nullable=False)
    fk_truck_type_id = db.Column('fk_truck_type_id',db.ForeignKey('truck_type.id'))
    price = db.Column('price',db.Integer,nullable=False)
    shipper_project_line = db.relationship("Shipper_project_line")
    truck_type = db.relationship("Truck_type")
    shipper = db.relationship("Shipper")
    line = db.relationship("Line")
    project = db.relationship("Project")
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    UniqueConstraint('fk_shipper_project_line_id', 'fk_truck_type_id', 'order_times')

    def __init__(self, fk_shipper_project_line_id, order_times, fk_truck_type_id, price):
        self.fk_shipper_project_line_id = fk_shipper_project_line_id
        self.price = price
        self.order_times = order_times
        self.fk_truck_type_id = fk_truck_type_id
    def __repr__(self):
        return '<Bid_line_price fk_project_id %r>' % self.fk_project_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict


class Bid_result(db.Model):
    __tablename__ = 'bid_result'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    fk_shipper_id = db.Column('fk_shipper_id',db.ForeignKey('shippers.id'))
    fk_line_id = db.Column('fk_line_id',db.ForeignKey('line.id'))
    fk_project_id = db.Column('fk_project_id',db.ForeignKey('project.id'))
    fk_user_id = db.Column('fk_user_id',db.ForeignKey('users.id'))
    status = db.Column('status',TINYINT(),default=0,nullable=False)
    shipper = db.relationship("Shipper")
    project = db.relationship("Project")
    line = db.relationship("Line")
    create_time = db.Column('create_time',db.TIMESTAMP,server_default=text('now()'))
    update_time = db.Column('update_time',db.TIMESTAMP)
    UniqueConstraint('fk_shipper_id', 'fk_line_id', 'fk_project_id')

    def __repr__(self):
        return '<Bid_result fk_project_id %r>' % self.fk_project_id

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        if 'create_time' in dict:
            del dict['create_time']
        return dict

