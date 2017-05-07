#coding:utf-8


from gevent import monkey
monkey.patch_all()
from gevent import wsgi

from camel.biz.application.flasksrv import FlaskApplication,instance,db


class CoroutineFlaskApplication(FlaskApplication):
    def __init__(self,*args,**kwargs):
        FlaskApplication.__init__(self,*args,**kwargs)
        # self.init()

    def run(self):
        http = self.conf.get('http')
        host = http.get('host','127.0.0.1')
        port = http.get('port',5000)
        app = self.getFlaskApp()
        server = wsgi.WSGIServer(( host, port), app)
        print 'Server: %s started, Listen on %s:%s ...'%(self.appName,host,port)
        server.serve_forever()

def setup(cls = CoroutineFlaskApplication):
    return cls.instance()

__all__=(CoroutineFlaskApplication,instance,db)