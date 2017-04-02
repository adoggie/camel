#coding:utf-8

from flask import Flask,g
from flask.ext.sqlalchemy import SQLAlchemy

from camel.fundamental.utils.useful import Instance
from camel.fundamental.application import Application,instance
from camel.biz.logging.filter import LogHandlerFilterMixer
from camel.biz.logging.handler import LogHandlerMixer

db = Instance()

class FlaskService(LogHandlerFilterMixer,LogHandlerMixer,Application):
    def __init__(self,*args,**kwargs):
        self.app = None     # flask app
        Application.__init__(self,*args,**kwargs)
        self.init()

    def getDatabase(self):
        return self.db

    def init(self):
        Application.init(self)
        self._initFlaskApp()

    def _initDatabase(self):
        global db
        if not self.db:
            self.db = SQLAlchemy()
            db.handle = self.db

    def _initFlaskApp(self):
        self.app = Flask(__name__)
        self._initFlaskConfig()
        self.getDatabase().init_app(self.app)
        self._initBlueprint()
        # g.instance = self

    def _initBlueprint(self):
        # if hasattr(self,'blueprint'):
        #     blueprints = self.blueprint
        #     for bp in blueprints:
        #         self.registerBlueprint( bp[0], bp[1] )
        # import urlparse

        rts = self.getRouteConfig()
        for rt in rts:
            url = rt.__url__
            appname = rt.__app__

            attrs = [s for s in dir(rt) if not s.startswith('__') ]
            for name in attrs:
                module = getattr(rt,name)
                bp = getattr(module,appname)
                splitchr = '/'
                if url[-1] =='/':
                    splitchr =''
                url_prefix = url+ splitchr  +bp.name
                print '>> init blueprint:',bp.name,' url_prefix:',url_prefix
                self.registerBlueprint(bp, url_prefix )

    def getRouteConfig(self):
        return []

    def _checkConfig(self):
        pass

    def _initFlaskConfig(self):
        """初始化激活的配置"""
        cfg = self.getConfig().get('flask_config')
        active = cfg.get('active')
        cfg_active = cfg.get(active)
        self.app.config.from_object( cfg_active)

    def _initLogger(self):
        from camel.biz.logging.logger import FlaskHttpRequestLogger
        return FlaskHttpRequestLogger(self.appName)

    def run(self):
        # Application.run(self)
        http = self.conf.get('http')
        if http:
            self.app.run(host=http.get('host','127.0.0.1'),
                port= http.get('port',5000),
                threaded= http.get('threaded',True),
                debug= http.get('debug',True))

    def registerBlueprint(self,bp,url):
        self.app.register_blueprint( bp , url_prefix= url )

def setup(cls = FlaskService):
    return cls.instance()

__all__=(db,FlaskService,instance)