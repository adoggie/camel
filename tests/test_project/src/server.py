#coding:utf-8


from camel.biz.application.flasksrv import FlaskApplication,setup,instance

class MyService(FlaskApplication):
    def __init__(self):
        FlaskApplication.__init__(self)

    # def getRouteConfig(self):
    #     return [ 'access.api.v1' ]

    # hooks as following
    def _initBefore(self):
        pass

    def _initAfter(self):
        pass

    def _requestBefore(self):
        FlaskApplication._requestBefore(self)
        print 'http request come in '

    def _requestTeardown(self,e):

        FlaskApplication._requestTeardown(self,e)
        print 'http request over.'

    def _requestAfter(self,response):
        FlaskApplication._requestAfter(self,response)
        return response

setup(MyService)

if __name__=='__main__':
    instance.run()


