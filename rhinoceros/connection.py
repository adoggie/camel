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

    def open(self):
        self.conn = psycopg2.connect(host=self.cfgs.get('host'),
            port=self.cfgs.get('port'),
            dbname = self.cfgs.get('dbname'),
            user = self.cfgs.get('user'),
            password = self.cfgs.get('password')
            )
        self.conn.autocommit = True
        return self.conn
