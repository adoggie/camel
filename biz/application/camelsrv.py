#coding:utf-8


from camel.fundamental.application import Application,instance

class CamelService(Application):
    def __init__(self,*args,**kwargs):
        Application.__init__(self,*args,**kwargs)
        self.init()

def setup(cls = CamelService):
    return cls.instance()

__all__=(CamelService,instance)