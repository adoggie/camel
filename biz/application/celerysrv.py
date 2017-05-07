#coding:utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from celery.bin import worker
from camel.biz.application.camelsrv import CamelApplication,db,instance
from camel.fundamental.celery.manager import CeleryManager

celery =None


class AsServer(object):
    def asServer(self): return True

class AsClient(object):
    def asServer(self): return False

class CeleryApplication(AsServer,CamelApplication):
    def __init__(self,*args,**kwargs):
        CamelApplication.__init__(self,*args,**kwargs)


    def _initAfter(self):
        global  celery
        celery = CeleryManager.instance().init(self.getConfig().get('celery_config', {})).app
        if self.asServer():
            CeleryManager.instance().current.open()

    @property
    def celeryManager(self):
        return CeleryManager.instance()

    def run(self):
        wkr = worker.worker(app = celery)
        options = {'loglevel': 'INFO', 'traceback': True, }
        wkr.run(**options)


class CeleryApplicationClient(AsClient,CeleryApplication):
    def __init__(self):
        CeleryApplication.__init__(self)

def setup(cls = CeleryApplication):
    return cls.instance()

__all__=(CeleryApplicationClient,CeleryApplication,AsServer,AsClient,instance,db,celery,setup)