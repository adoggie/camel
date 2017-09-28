#coding:utf-8

"""
srvmgr.py
 服务管理
"""
import gevent
import json
from camel.fundamental.utils.useful import Singleton
from camel.fundamental.utils.importutils import import_function

class ServiceManager(Singleton):
    def __init__(self):
        self.endpoints = []
        self.tasks = []

    def addEndpoint(self,endpoint):
        self.endpoints.append( endpoint )

    def register_http_service(self,api_list):
        """注册 http api 接口

        :param api_list:
            { module_name:array({url,methods}) , .. }
        :return:
        """
        for ep in self.endpoints:
            ep.register_http_service(api_list)
        return self

    def addWatchTask(self,task_cfgs):
        wrapper = ServiceWatchTaskExecutor(task_cfgs)
        self.tasks.append( wrapper )

    def startWatch(self):
        for task in self.tasks:
            task.start()

    def stopWatch(self):
        for task in self.tasks:
            task.stop()

class ServiceWatchTaskExecutor(object):

    def __init__(self,cfgs):
        task = import_function(cfgs.get('entry'))
        self.task_entry = task
        self.cfgs = cfgs
        self.interval = int(self.cfgs.get('interval',10))
        self.running = False
        self.tasklet = None



    def start(self):
        self.tasklet = gevent.spawn(self.execute)

    def stop(self):
        self.running = False
        gevent.joinall([self.tasklet])

    def execute(self):
        self.running = True
        while self.running:
            gevent.sleep(self.interval)
            repeated = self.task_entry(self.cfgs)
            if not repeated:
                break



class ServiceRegEndpointZookeeper(object):
    def __init__(self,zkclient,workdir):
        """
        :param zkclient: zk -  camel.fundamental.zookeeper.client.ZKClient
        :param workdir:  服务注册目录
        workdir下创建 http_service 条目用于记录服务api
        """
        self.zk = zkclient
        self.workdir = workdir

    def register_http_service(self,api_list):
        """

        :param api_list:
            { module_name:array({url,methods}) , .. }
        :return:
        """
        data = api_list
        if isinstance(api_list,dict):
            data = json.dumps(api_list)
        if isinstance(data,str) :
            node = self.workdir+'/http_service'
            self.zk.createNode(node)
            self.zk.setNodeData(node,data)


