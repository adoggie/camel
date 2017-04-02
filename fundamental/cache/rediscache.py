#coding:utf-8

# from flask.ext.redis import FlaskRedis

class RedisCache:
    def __init__(self,name,cfg):
        self.type = cfg.get('type').lower()
        self.name = name
        self.cfg = cfg
        # self.handle = FlaskRedis()
        # self.h = self.handle




