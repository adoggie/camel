#coding:utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from camel.fundamental.utils.useful import Instance
from camel.fundamental.application import Application,instance

db = Instance()

class CamelApplication(Application):
    def __init__(self,*args,**kwargs):
        Application.__init__(self,*args,**kwargs)
        self.flask_app = None
        self.init()
        self._initSignal()
        self._initFlaskApp()

    def _initSignal(self):
        """多线程时, signal 被发送到创建的子线程中，主线程无法捕获"""
        import signal
        signal.signal(signal.SIGINT, self._sigHandler)

    def _sigHandler(self,signum, frame):
        print 'signal ctrl-c'
        self._terminate()

    def _terminate(self):
        pass

    def _initDatabase(self):
        pass

    def _initFlaskApp(self):
        self.app = Flask(__name__)
        self._initFlaskConfig()
        self._initFlaskCors()

        # global db
        if db.get() is None:
            self.db = SQLAlchemy(self.app)
            db.handle = self.db

    def getDatabase(self):
        return self.db

    def getFlaskConfig(self):
        cfg = self.getConfig().get('flask_config')
        return cfg.get( cfg.get('active') )


    def _initFlaskConfig(self):
        """初始化激活的配置"""
        active = self.getFlaskConfig()
        for k, v in active.items():
            self.app.config[k] = v

    def _initFlaskCors(self):
        """
            https://flask-cors.readthedocs.io/en/latest/
        :return:
        """
        CORS(self.app)

    def getFlaskApp(self):
        return self.app

def setup(cls = CamelApplication):
    return cls.instance()

__all__=(CamelApplication,instance,db)