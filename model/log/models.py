#-*- coding:utf-8 -*-
#! /usr/bin/env python

"""
Model module for yto.camel's LOG system.
"""

# History
# -------
#
# George Gao started this module.George Gao
# reformatted and documented the module and
# is currently responsible for its maintenance.
#

__version__ = "0.1"
__author__ = "GYZ"
__date__ = "2016-05-10"


# Imports
# =======

from camel.biz.application.camelsrv import db


# Classes for field storage
# =========================

class Camellog(db.Model):
    __tablename__ = 'camellog'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    create_time = db.Column('create_time',db.String(32),nullable=True)
    device_id = db.Column('device_id',db.String(40),nullable=True)
    mobile = db.Column('mobile',db.String(16),index=True,nullable=True)
    lon = db.Column('lon', db.Integer,nullable=True)
    lat = db.Column('lat', db.Integer,nullable=True)
    address = db.Column('address', db.String(128),nullable=True)
    device_model = db.Column('device_model', db.String(32),nullable=True)
    log_type = db.Column('log_type', db.String(16),nullable=True)
    trans_number = db.Column('trans_number', db.String(32),index=True,nullable=True)
    app_ver = db.Column('app_ver', db.String(32),nullable=True)


    def __repr__(self):
        return '<Camellog mobile %r>' % self.mobile

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict


class Online(db.Model):
    __tablename__ = 'online'

    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    get_time = db.Column('get_time',db.String(32),nullable=True)
    mobile = db.Column('mobile',db.String(16),index=True,nullable=False)
    lon = db.Column('lon', db.Integer,nullable=True)
    lat = db.Column('lat', db.Integer,nullable=True)
    trans_number = db.Column('trans_number', db.String(32),index=True,nullable=True)
    mem = db.Column('mem', db.Integer,nullable=True)
    battery = db.Column('battery', db.Integer,nullable=True)


    def __repr__(self):
        return '<Online mobile %r>' % self.mobile

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        return dict
