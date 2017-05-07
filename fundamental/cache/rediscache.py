#coding:utf-8

# from flask.ext.redis import FlaskRedis
import redis

"""
https://pypi.python.org/pypi/redis
https://redis.io/topics/quickstart

https://redislabs.com/lp/python-redis/

http://www.runoob.com/redis/redis-lists.html


"""

class RedisCache:
    def __init__(self,cfg):
        self.type = cfg.get('type').lower()
        self.name = cfg.get('name')
        self.cfg = cfg
        self.h = None

    def open(self):
        host = self.cfg.get('host')
        port = self.cfg.get('port')
        passwd = self.cfg.get('password')
        self.h = redis.StrictRedis(host, port,password=passwd)
        return True

    def get(self, key):
        return self.h.get(key)

    def set(self, key, value, expire=None):
        self.h.set(key, value, expire)

    def delete(self, key):
        self.h.delete(key)

