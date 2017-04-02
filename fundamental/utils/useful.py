#coding:utf-8


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda : instance
    return instance

class Singleton(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls,'handle'):
            cls.handle = cls()
        return cls.handle

class Instance:
    def __init__(self):
        self.handle = None

    def set(self,handle):
        self.handle = handle

    def __getattr__(self, item):
        return getattr(self.handle,item)

    def get(self):
        return self.handle


def hash_object(obj):
    attrs = [s for  s in dir(obj) if not s.startswith('__')  ]
    kvs={}
    for k in attrs:
        attr = getattr(obj, k)
        if not callable(attr):
            kvs[k] = attr
    return kvs