#coding:utf-8

import sys
import getopt

from camel.biz.application.celerysrv import CeleryApplication,AsClient,setup,instance,celery

class MyService(AsClient,CeleryApplication):
    def __init__(self):
        CeleryApplication.__init__(self)

setup(MyService)

instance.celeryManager.getService('test_server').send_task('access.celery.hello.hello',args=['sss',])



