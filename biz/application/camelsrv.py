#coding:utf-8


from camel.fundamental.application import Application,instance
from camel.biz.logging.filter import LogHandlerFilterMixer
from camel.biz.logging.handler import LogHandlerMixer

class CamelService(LogHandlerFilterMixer,LogHandlerMixer,Application):
    def __init__(self,*args,**kwargs):
        Application.__init__(self,*args,**kwargs)
        self.init()

    def _initLogger(self):
        from camel.biz.logging.logger import CamelLogger
        return CamelLogger(self.appName)


def setup(cls = CamelService):
    return cls.instance()

__all__=(CamelService,instance)