#coding:utf-8

import use_gevent
from use_gevent import Event
from camel.fundamental.utils.useful import Instance
from camel.fundamental.application import Application,instance


class CamelApplication(Application):
    def __init__(self,*args,**kwargs):
        Application.__init__(self,*args,**kwargs)
        self.wait_ev = Event()
        self.init()
        self._initSignal()

    def _initSignal(self):
        """多线程时, signal 被发送到创建的子线程中，主线程无法捕获"""
        import signal
        signal.signal(signal.SIGINT, self._sigHandler)

    def _sigHandler(self,signum, frame):
        print 'signal ctrl-c'
        self._terminate()

    def _initDatabase(self):
        pass

    def run(self):
        print 'Camel Server starting..'
        Application.run(self)

    def serve_forever(self):
        while not self.wait_ev.is_set():
            self.wait_ev.wait(1)

    def _terminate(self):
        self.wait_ev.set()

    def _setupZk(self):
        from camel.fundamental.zookeeper.client import ZKClient
        cfg = self.getConfig().get('zookeeper_config')
        if cfg:
            self.zk = ZKClient(cfg)
            self.zk.open()

    def getZookeeper(self):
        return self.zk

    def _setupCelery(self):
        from camel.fundamental.celery.manager import CeleryManager
        CeleryManager.instance().init(self.getConfig().get('celery_config', {}))
        if CeleryManager.instance().current:
            CeleryManager.instance().current.open()

    def _setupKafka(self):
        from camel.fundamental.kafka import KafkaManager
        KafkaManager.instance().init(self.getConfig().get('kafka_config'))


    def _setupAmqp(self):
        from camel.fundamental.amqp import AmqpManager
        AmqpManager.instance().init(self.getConfig().get('amqp_config'))

    def _setupServiceManager(self):
        # 服务管理器
        from srvmgr import ServiceManager, ServiceRegEndpointZookeeper
        ServiceManager.instance()
        workdir = "%s/%s" % (self.projectName, self.appName)
        if self.zk:
            sre = ServiceRegEndpointZookeeper(self.zk, workdir)
            ServiceManager.instance().addEndpoint(sre)

        cfgs = self.getConfig().get('watchtask_config',[])
        for cfg in cfgs:
            ServiceManager.instance().addWatchTask(cfg)
        ServiceManager.instance().startWatch()

    def _initAfter(self):
        super(CamelApplication,self)._initAfter()
        self._setupCelery()
        self._setupAmqp()
        self._setupKafka()
        self._setupZk()
        self._setupServiceManager()


def setup(cls = CamelApplication):
    return cls.instance()

__all__=(CamelApplication,instance)