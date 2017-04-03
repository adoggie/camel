#coding:utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from camel.fundamental.utils.importutils import *
from camel.fundamental.utils.useful import Instance,ObjectCreateHelper
from camel.fundamental.application import Application,instance
from camelsrv import CamelService

db = Instance()
# er = Obj# db.helpectCreateHelper(lambda :SQLAlchemy())

# class FlaskService(LogHandlerFilterMixer,LogHandlerMixer,Application):
class FlaskService( CamelService):
    def __init__(self,*args,**kwargs):
        self.app = None     # flask app
        CamelService.__init__(self,*args,**kwargs)

    def getDatabase(self):
        return self.db

    def getFlaskConfig(self):
        cfg = self.getConfig().get('flask_config')
        return cfg.get( cfg.get('active') )

    def init(self):
        Application.init(self)
        self._initFlaskApp()

    def _initDatabase(self):
        pass

    def getFlaskApp(self):
        return self.app

    def _initFlaskApp(self):
        self.app = Flask(__name__)
        self._initFlaskConfig()

        global db
        if db.get() is None:
            self.db = SQLAlchemy(self.app)
            db.handle = self.db
        # else: # db 先被创建，然后绑定Flask app
            # db.handle.init_app( self.app )
            # db.handle.app = self.app

        self._initBlueprint()

    # def _recursive_import(self,path):

    def _initBlueprint(self):

        rts = self.getRouteConfig()
        for rt in rts:
            rt = import_module( rt )
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

        active = self.getFlaskConfig()
        # self.app.config.from_object( cfg_active)
        for k,v in active.items():
            self.app.config[k] = v

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




__all__=(db,FlaskService,instance,setup)