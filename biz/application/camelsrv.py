#coding:utf-8

from camel.fundamental.utils.useful import Instance
from camel.fundamental.application import Application,instance


db = Instance()

class CamelApplication(Application):
    def __init__(self,*args,**kwargs):
        Application.__init__(self,*args,**kwargs)
        self.init()

def setup(cls = CamelApplication):
    return cls.instance()

__all__=(CamelApplication,instance,db)