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

    def _initDatabase(self):
        self.app = Flask(__name__)
        cfgs = self.getConfig().get('database_config')
        for k,v in cfgs.items():
            self.app.config[k] = v

        if db.get() is None:
            self.db = SQLAlchemy(self.app)
            db.handle = self.db

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


def setup(cls = CeleryApplication):
    return cls.instance()

__all__=(CeleryApplication,AsServer,AsClient,instance,db,celery,setup)