#coding:utf-8


"""
https://github.com/libwilliam/flask-compress
https://github.com/closeio/Flask-gzip

"""
from gevent import wsgi
from flask import Flask,request,g
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_compress import Compress
from flask.ext.gzip import Gzip


from camel.fundamental.utils.importutils import *
from camel.fundamental.utils.useful import Instance
from camel.fundamental.application import Application,instance
from camel.biz.application.srvmgr import ServiceManager

from camelsrv import CamelApplication


db = Instance()

class FlaskApplication( CamelApplication):
    def __init__(self,*args,**kwargs):
        self.app = None
        self.api_list = {}  # 注册api

        if kwargs.get('db_init',False):
            Application.__init__(self)
            self._initConfig()
        else:
            CamelApplication.__init__(self,*args,**kwargs)
        self._initFlaskApp()

    def _initFlaskApp(self,app=None):
        if not app:
            app = Flask(__name__)  # flask会自动将当前代码目录设置为项目根目录 root_path 导致读取templtes , sta它ic 目录失败
        self.app = app
        Compress(app)  # okay
        # gzip = Gzip(app) # error

        self._initFlaskConfig()
        self._initFlaskCors()

        global db
        if db.get() is None:
            self.db = SQLAlchemy(self.app)
            db.handle = self.db

        self._initRequestHooks()
        self._initBlueprint()

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

    def _initRequestHooks(self):
        self.app.before_request(self._requestBefore)
        self.app.teardown_request(self._requestTeardown)
        # self.app.after_request(self._requestAfter)  # todo. 导致 send_file 失败
        # 当利用send_file发送二进制数据时，after_request对返回数据进行日志处理，导致数据返回失败

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
        # pass
        import time
        g.start_time = time.time()

        #
        # trace = self.getConfig().get('http_trace',{}).get('request',{})
        # options = trace.get('options',{'header':False,'body':False,'max_size':1024})
        # urls = trace.get('urls',[])
        # #sort urls by 'match' with desceding.
        # urls = sorted(urls,cmp = lambda x,y: cmp(len(x.get('match')) , len(y.get('match')) ) )
        # urls.reverse()
        #
        # text = ''
        # for url in urls:
        #     m = url.get('match')
        #     if m:
        #         opts = options.copy()
        #         opts['header'] = url.get('header',options.get('header'))
        #         opts['body'] = url.get('body',options.get('body'))
        #         opts['max_size'] = url.get('max_size',options.get('max_size'))
        #         if request.url.find(m) !=-1:
        #             text = self._traceRequestInfo(opts)
        #             break
        # level = self.getConfig().get('http_trace',{}).get('level','DEBUG')
        # text = 'HttpRequest: '+text
        # self.getLogger().log(level,text)

    def _requestTeardown(self,e):
        pass

    def _requestAfter(self,response):
        import time


        trace = self.getConfig().get('http_trace', {}).get('response', {})
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
        level = self.getConfig().get('http_trace', {}).get('level', 'DEBUG')

        remote_addr = ''
        if request.headers.getlist("X-Forwarded-For"):
            remote_addr = request.headers.getlist("X-Forwarded-For")[0]
        else:
            remote_addr = request.remote_addr

        elapsed = int((time.time() - g.start_time) * 1000)
        text = 'HTTP %s %s %s %sms  '%( remote_addr ,request.method,request.url,elapsed)
        self.getLogger().log(level, text)

        return response

    def _initBlueprint(self):
        from flask import Blueprint

        self.blueprints = {}

        cfgs = self.getConfig().get('blueprint_routes',[])
        for cfg in cfgs:
            # module = import_module( cfgs.get('module'))
            package_name = cfg.get('name','')
            package = cfg.get('package')
            package_url = cfg.get('url')
            modules = cfg.get('modules',[])
            for module in modules:
                module_name = module.get('name',)
                module_url = module.get("url",'')
                path = '%s.%s'%(package,module_name)
                load_module = import_module(path)

                app = Blueprint(module_name,path)
                self.blueprints[path] = app

                # api_module = {'name': u'%s.%s'%(package_name,module_name),'api_list':[]}
                module_name = u'%s.%s'%(package_name,module_name)
                self.api_list[module_name] = []

                routes = module.get('routes',[])
                for route in routes:
                    url = route.get('url','')
                    name = route.get('name','')
                    methods = filter(lambda x:len(x)>0,route.get('methods','').strip().upper().split(','))

                    if hasattr( load_module,name):
                        func = getattr( load_module,name)
                        path = package_url+module_url
                        path  = path.replace('//','/')
                        if methods:
                            app.route(url,methods=methods)(func)
                        else:
                            app.route(url)(func)
                        self.registerBlueprint(app,path)
                        path = path + '/' + url
                        path = path.replace('//','/')
                        instance.getLogger().debug('registered blueprint route:'+path)

                        api = {'url': path,
                                'methods': ('GET',)}

                        if methods:
                            api['methods'] = methods
                        self.api_list[module_name].append(api)

            ServiceManager.instance().register_http_service(self.api_list)

    def getRouteConfig(self):
        return self.conf.get('blueprint_routes')

    def _checkConfig(self):
        pass

    def _initLogger(self):
        from camel.biz.logging.logger import FlaskHttpRequestLogger
        return FlaskHttpRequestLogger(self.appId)

    def run(self):
        # Application.run(self)
        http = self.conf.get('http')
        if http:
            self.app.run(host=http.get('host','127.0.0.1'),
                port= http.get('port',5000),
                threaded= http.get('threaded',True),
                debug= http.get('debug',True),
                process=http.get('process',1))

    def registerBlueprint(self,bp,url):
        self.app.register_blueprint( bp , url_prefix= url )


class ServiceFlaskApplication(FlaskApplication):
    def __init__(self,*args,**kwargs):
        FlaskApplication.__init__(self,*args,**kwargs)
        self.server = None

    def run(self):
        http = self.conf.get('http')
        host = http.get('host','127.0.0.1')
        port = http.get('port',5000)
        app = self.getFlaskApp()

        print 'Server: %s started, Listen on %s:%s ...' % (self.appId, host, port)

        if http.get('debug',False):
            app.run(host,port,debug=True)
        else:
            self.server = wsgi.WSGIServer(( host, port), app)

            self.server.start()
            Application.run(self)

    def serve_forever(self):
        self.server.serve_forever()

def setup(cls = ServiceFlaskApplication):
    return cls.instance()


__all__=(db,FlaskApplication,ServiceFlaskApplication,instance,setup)