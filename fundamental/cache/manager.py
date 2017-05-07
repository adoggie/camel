#coding:utf-8

from camel.fundamental.utils.useful import Singleton

from rediscache import RedisCache

class CacheManager(Singleton):
    def __init__(self):
        self.cfgs = None
        self.caches ={}

    def get(self,name='default'):
        return self.caches.get(name)

    def init(self,cfgs):
        """加载缓冲设备项目"""
        if not cfgs:
            return

        for name,cfg in cfgs.items():
            cache = None
            if cfg.get('type').lower() == 'redis' and cfg.get('enable') == True:
                cache = RedisCache(cfg)
                cache.open()
                self.caches[name] = cache
        return self