#coding:utf-8

import unittest



class testApp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app(self):
        # print Application().instance()
        pass

    def test_config(self):
        pass
        # self.app.init()
        # print self.app.getCamelHomePath()
        # print self.app.getConfig()

    def test_camelservice(self):
        from camel.biz.application.camelsrv import setup
        setup()
        from camel.biz.application.camelsrv import instance

        app = instance

        app.getLogger().addTag('CS')
        app.getLogger().debug('first line',tags='HOP,TRANS:A00912')
        app.getLogger().error('http request timeout',tags='HOP,TRANS:A00912')
        app.getLogger().removeTag('CS')
        app.getLogger().setTags('HOPE,ENT')

        app.getLogger().debug('xxxx')
        app.getLogger().setTransportTag('AK100001') #设置承运商
        app.getLogger().debug('request in ')
        print instance.getConfigPath()


    def xtest_flaskservice(self):
        from camel.biz.application.flasksrv import setup
        setup()
        from camel.biz.application.flasksrv import instance

        app = instance

        app.getLogger().addTag('CS')
        app.getLogger().debug('first line', tags='HOP,TRANS:A00912')
        app.getLogger().error('http request timeout', tags='HOP,TRANS:A00912')
        app.getLogger().removeTag('CS')
        app.getLogger().setTags('HOPE,ENT')

        app.getLogger().debug('xxxx')
        app.getLogger().setTransportTag('AK100001')  # 设置承运商
        app.getLogger().debug('request in ')

