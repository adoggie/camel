#coding:utf-8



from gevent import monkey
monkey.patch_all(Event=True)
from gevent.event import Event
import gevent

from threading import Event
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from camel.biz.application.camelsrv import CamelApplication,db,instance

class CoroutineApplication(CamelApplication):
    def __init__(self,*args,**kwargs):
        CamelApplication.__init__(self,*args,**kwargs)
        self.wait_ev = Event()

    def run(self):
        print 'Coroutine Server starting..'
        while not self.wait_ev.is_set():
            self.wait_ev.wait(1)

    def _terminate(self):
        self.wait_ev.set()

def setup(cls = CoroutineApplication):
    return cls.instance()

__all__=(CoroutineApplication,instance,db,setup)