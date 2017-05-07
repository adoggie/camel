#coding:utf-8

__doc__=u'zkclient '

class ZKClient(object):
    def __init__(self,cfg):
        self.cfg = cfg

    def init(self,*args,**kwargs):
        pass

    def open(self):
        pass

    def onWatch(self,ev):
        pass

    def getNodeData(self,node):
        pass

    def setNodeData(self,node,data):
        pass

    def createNode(self,node):
        pass

    def removeNode(self,node):
        pass

    def setRootNode(self,node):
        pass
