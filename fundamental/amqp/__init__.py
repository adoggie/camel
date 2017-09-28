#coding:utf-8

from camel.fundamental.utils.useful import Singleton
from camel.fundamental.amqp.base import MessageQueueType,AccessMode

from camel.fundamental.amqp.conn_qpid import MQConnectionQpid


class AmqpManager(Singleton):
    def __init__(self):
        self.cfgs = None
        self.queues = {}

    def init(self,cfgs):
        if not cfgs:
            return
        self.cfgs = cfgs
        for cfg in self.cfgs:
            if cfg.get('enable',False) is False:
                continue
            mq = MQConnectionQpid(cfg)
            self.queues[mq.name] = mq
            readwrite = 0
            if cfg.get('write',False):
                readwrite |= AccessMode.WRITE
            if cfg.get('read',False):
                readwrite |= AccessMode.READ
            mq.open(readwrite)

        return self

    def getMessageQueue(self,name):
        return self.queues.get(name)

    def terminate(self):
        for mq in self.queues.values():
            mq.close()