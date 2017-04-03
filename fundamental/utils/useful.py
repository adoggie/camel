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

class ObjectCreateHelper(object):
    def __init__(self,func,*args,**kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def create(self):
        return self.func(*self.args,**self.kwargs)

class Instance(object):
    def __init__(self):
        self.handle = None
        self.helper = None

    def set(self,handle):
        self.handle = handle

    def __getattr__(self, item):
        return getattr(self.handle, item)

        # if self.handle:
        #     return getattr(self.handle,item)
        # if  self.helper:
        #     v = self.helper.create()
        #     return v


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