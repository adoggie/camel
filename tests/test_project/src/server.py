#coding:utf-8


from camel.biz.application.flasksrv import FlaskService,setup,instance

class MyService(FlaskService):
    def __init__(self):
        FlaskService.__init__(self)

    def getRouteConfig(self):
        return [ 'route.v1' ]

    # hooks as following
    def _init_before(self):
        pass

    def _init_after(self):
        pass

setup(MyService)

if __name__=='__main__':
    instance.run()


