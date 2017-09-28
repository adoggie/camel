#coding:utf-8


import psycopg2,psycogreen
import gevent_psycopg2
gevent_psycopg2.monkey_patch()

"""
每台车辆
"""


class PostgreSqlConnection(object):
    """
        https://pypi.python.org/pypi/psycopg2
        http://pythonhosted.org/psycopg2/
        http://initd.org/psycopg/

        postgresql 9.4+
        psycopg2 2.7+
        jsonb supported: 2.5.4+
                http://initd.org/psycopg/docs/extras.html


        dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    """
    def __init__(self,cfgs):
        self.cfgs = cfgs
        self.name = self.cfgs.get('name','')
        self.conn = None
        self.pool = None

    def open(self):
        self.conn = psycopg2.connect(host=self.cfgs.get('host'),
            port=self.cfgs.get('port'),
            dbname = self.cfgs.get('dbname'),
            user = self.cfgs.get('user'),
            password = self.cfgs.get('password')
            )
        self.conn.autocommit = True
        return self.conn



class DatabaseConnectionPool(object):
    def __init__(self,cfgs):
        self.cfgs = cfgs
        self.conns = []

    def init(self,size=5):
        size = self.cfgs.get('pool_size',size)

        for _ in xrange(size):
            conn = None
            driver = self.cfgs.get('driver','pgsql')
            if driver == 'pgsql':
                conn = PostgreSqlConnection(self.cfgs).open()
            if conn:
                conn.pool = self
                self.conns.append(conn)
        return self

    def getConnection(self):
        conn = None
        if self.conns:
            conn = self.conns[0]
            del self.conns[0]
        return conn

    def freeConnection(self,conn):
        if self.conns.count(conn) == 0:
            self.conns.append(conn)


