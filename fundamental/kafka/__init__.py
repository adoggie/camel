#coding:utf-8


"""
author: sam
revision:
    1. create 2017/4/8
"""

from threading import Thread,Condition,Lock
from pykafka import  KafkaClient
from pykafka.common import OffsetType
from camel.fundamental.utils.useful import Singleton
from camel.fundamental.utils.importutils import import_function

READ  = 0x01
WRITE = 0x02
RW = READ|WRITE

class KafkaTopic(object):
    def __init__(self,cfg):
        self.name = cfg.get('topic')
        self.group = cfg.get('group','')
        self.hosts = cfg.get('hosts')
        self.zookeepers = cfg.get('zookeepers')
        self.execthread_nr = cfg.get('exec_thread_nr',1)
        self.entry = cfg.get('entry')
        self.corutine = cfg.get('corutine',False)
        self.access_cfg = filter(lambda x: len(x)>0,cfg.get('access','').strip().upper().split(',') )
        self.conn = None
        self.topic = None
        self.producer = None
        self.consumer = None
        self.cond_readable = Condition()
        self.thread = None
        self.isclosed = True
        self.execthreads = []
        self.message_pool = []
        self.lock = Lock()

        self.func_list ={} #导入的函数列表


    def open(self,access=READ):
        if  access == 0:
            return self

        if not self.conn:
            self.conn = KafkaClient(hosts=self.hosts)
            self.topic = self.conn.topics[self.name]

        if access & READ:
            if not self.consumer:
                if self.group:
                    self.consumer = self.topic.get_balanced_consumer(consumer_group=self.group,
                                auto_commit_enable=True,
                                reset_offset_on_start = True,auto_offset_reset=OffsetType.LATEST,
                                zookeeper_connect= self.zookeepers
                                )
                else:
                    self.consumer = self.topic.get_simple_consumer(auto_commit_enable=True,
                            reset_offset_on_start = True,auto_offset_reset=OffsetType.LATEST
                            )
                func = import_function( self.entry ) # importing functions dynamically
                self.func_list[self.entry] = func

                self.thread = Thread(target=self._messageRecieving)
                self.thread.start()
        if access & WRITE:
            if not self.producer:
                self.producer = self.topic.get_producer(delivery_reports=False)

        return self

    def close(self):
        self.isclosed = True
        with self.cond_readable:
            self.cond_readable.notify_all()
        if self.consumer:
            print 'invoke consumer stop()'
            self.consumer.stop()
        self.thread.join()

    def _executeThread(self):
        """多线程"""
        while not self.isclosed:
            with self.cond_readable:
                self.cond_readable.wait()
            if self.isclosed:
                break
            message = None
            self.lock.acquire()
            if len(self.message_pool):
                message = self.message_pool[0]
                del self.message_pool[0]
            self.lock.release()

            if message is not None:
                func = self.func_list[self.entry]
                func(message) # pass into user space
        print 'topic read thread is exiting..'

    def produce(self,message):
        self.producer.produce(message)

    def _messageRecieving(self):
        """消息接收线程,保证一个线程接收"""
        self.isclosed = False
        for nr in range(self.execthread_nr):
            thread = Thread(target=self._executeThread)
            self.execthreads.append(thread)
            thread.start()

        while not self.isclosed:
            for message in self.consumer:
                if message is not None:
                    # print message.offset, message.value
                    self.consumer.commit_offsets()
                    self.lock.acquire()
                    self.message_pool.append(message.value)
                    self.lock.release()
                    with self.cond_readable:
                        self.cond_readable.notify()


        for thread in self.execthreads:
            thread.join()
        print 'topic main thread is exiting...'

class KafkaManager(Singleton):
    def __init__(self):
        self.cfgs = None
        self.topics = {}

    def init(self,cfgs):
        if not cfgs: return

        self.cfgs = cfgs
        for cfg in self.cfgs:
            if cfg.get('enable',False) is False:
                continue
            topic = KafkaTopic(cfg)
            self.topics[topic.name] = topic

            readwrite = 0
            if cfg.get('write',False):
                readwrite |= WRITE
            if cfg.get('read',False):
                readwrite |= READ

            topic.open(readwrite)

        return self

    def getTopic(self,name):
        return self.topics.get(name)

    def terminate(self):
        for topic in self.topics.values():
            topic.close()

__all__ = (KafkaManager,KafkaTopic)