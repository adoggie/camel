#coding:utf-8

from flask import Flask,request,g
from flask.ext.sqlalchemy import SQLAlchemy

from camel.fundamental.utils.importutils import *
# from camel.fundamental.utils.useful import Instance,ObjectCreateHelper
from camel.fundamental.application import Application,instance
from camelsrv import CamelApplication,db

# db = Instance()
# er = Obj# db.helpectCreateHelper(lambda :SQLAlchemy())

class FlaskApplication( CamelApplication):
    def __init__(self,*args,**kwargs):
        self.app = None     # flask app
        CamelApplication.__init__(self,*args,**kwargs)

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

        # global db
        if db.get() is None:
            self.db = SQLAlchemy(self.app)
            db.handle = self.db

        self._initRequestHooks()
        self._initBlueprint()


    def _initRequestHooks(self):
        self.app.before_request(self._requestBefore)

        self.app.teardown_request(self._requestTeardown)
        self.app.after_request(self._requestAfter)

    def _traceRequestInfo(self,opts):
        import json
        trace_data = {'url':request.url}
        if opts.get('header'):
            trace_data['headers'] = request.headers
        if opts.get('body'):
            trace_data['body'] = request.data.replace('\n',' ')[:opts.get('max_size')]
        return json.dumps( trace_data)

    def _traceResponseInfo(self,opts,response):
        import json
        trace_data = {'url':request.url}
        if opts.get('header'):
            trace_data['headers'] = response.headers
        if opts.get('body'):
            trace_data['body'] = response.data.replace('\n',' ')[:opts.get('max_size')]
        return json.dumps( trace_data)

    def _requestBefore(self):
        import time
        g.start_time = time.time()

        trace = self.getConfig().get('auto_trace',{}).get('http_request',{})
        options = trace.get('options',{'header':False,'body':False,'max_size':1024})
        urls = trace.get('urls',[])
        #sort urls by 'match' with desceding.
        urls = sorted(urls,cmp = lambda x,y: cmp(len(x.get('match')) , len(y.get('match')) ) )
        urls.reverse()


        text = ''
        for url in urls:
            m = url.get('match')
            if m:
                opts = options.copy()
                opts['header'] = url.get('header',options.get('header'))
                opts['body'] = url.get('body',options.get('body'))
                opts['max_size'] = url.get('max_size',options.get('max_size'))
                if request.url.find(m) !=-1:
                    text = self._traceRequestInfo(opts)
                    break
        level = self.getConfig().get('auto_trace',{}).get('level','DEBUG')
        text = 'HttpRequest: '+text
        self.getLogger().log(level,text)

    def _requestTeardown(self,e):
        pass

    def _requestAfter(self,response):
        import time
        elapsed = int( (time.time() - g.start_time)*1000 )

        trace = self.getConfig().get('auto_trace', {}).get('http_response', {})
        options = trace.get('options', {'header': False, 'body': False, 'max_size': 1024})
        urls = trace.get('urls', [])

        urls = sorted(urls, cmp=lambda x, y: cmp(len(x.get('match')), len(y.get('match'))))
        urls.reverse()

        text = ''
        for url in urls:
            m = url.get('match')
            if m:
                opts = options.copy()
                opts['header'] = url.get('header', options.get('header'))
                opts['body'] = url.get('body', options.get('body'))
                opts['max_size'] = url.get('max_size', options.get('max_size'))
                if request.url.find(m) != -1:
                    text = self._traceResponseInfo(opts,response)
                    break
        level = self.getConfig().get('auto_trace', {}).get('level', 'DEBUG')

        text = 'HttpResponse (elapsed time:%sms) : '%elapsed + text
        self.getLogger().log(level, text)

        return response

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
        return self.conf.get('blueprint_routes',[])

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

def setup(cls = FlaskApplication):
    return cls.instance()




__all__=(db,FlaskApplication,instance,setup)