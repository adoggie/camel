#coding:utf-8

import os
import psycogreen.gevent
psycogreen.gevent.patch_psycopg()
from gevent.pywsgi import WSGIServer

import django
from django.core.handlers.wsgi import WSGIHandler


from gevent import wsgi
# from camel.fundamental.application.app import Application
from camel.biz.application.camelsrv import CamelApplication,instance


class ServiceDjangoApplication(CamelApplication):
    def __init__(self,*args,**kwargs):
        CamelApplication.__init__(self,*args,**kwargs)
        self.server = None

    def _initBefore(self):
        pass

    def _initConfig(self):
        super(ServiceDjangoApplication,self)._initConfig()
        settings = self.getConfig().get('django_settings','django.settings')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
        django.setup()

    def run(self):
        http = self.conf.get('http')
        host = http.get('host','127.0.0.1')
        port = http.get('port',5000)
        address = (host,port)
        self.server = WSGIServer(address, WSGIHandler())

        print 'Server: %s started, Listen on %s:%s ...'%(self.appId,host,port)
        self.server.start()
        super(ServiceDjangoApplication, self).run()

    def serve_forever(self):
        self.server.serve_forever()

def setup(cls = ServiceDjangoApplication):
    return cls.instance()

__all__=(ServiceDjangoApplication,instance)