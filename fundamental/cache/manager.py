#coding:utf-8



class CacheManager(object):
    def __init__(self):
        self.caches ={}

    def get(self,name='default'):
        return self.caches.get(name)

    def loads(self,cfgs):
        """加载缓冲设备项目"""
        if not cfgs:
            return

        for name,cfg in cfgs.items():
            cache = None
            if cfg.get('type').lower() == 'redis' and cfg.get('enable') == True:
                import rediscache
                cache = rediscache.RedisCache( name,cfg)
            if cache:
                self.caches[name] = cache
        return self