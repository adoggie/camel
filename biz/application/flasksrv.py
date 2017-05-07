#coding:utf-8

from flask import Flask,request,g
from flask.ext.sqlalchemy import SQLAlchemy


from camel.fundamental.utils.importutils import *
from camel.fundamental.application import Application,instance
from camelsrv import CamelApplication,db


class FlaskApplication( CamelApplication):
    def __init__(self,*args,**kwargs):
        CamelApplication.__init__(self,*args,**kwargs)

    def _initFlaskApp(self):
        CamelApplication._initFlaskApp(self)
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

        trace = self.getConfig().get('http_trace',{}).get('request',{})
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
        level = self.getConfig().get('http_trace',{}).get('level','DEBUG')
        text = 'HttpRequest: '+text
        self.getLogger().log(level,text)

    def _requestTeardown(self,e):
        pass

    def _requestAfter(self,response):
        import time
        elapsed = int( (time.time() - g.start_time)*1000 )

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

        text = 'HttpResponse (elapsed time:%sms) : '%elapsed + text
        self.getLogger().log(level, text)

        return response

    def _initBlueprint(self):
        from flask import Blueprint

        self.blueprints = {}

        cfgs = self.getConfig().get('blueprint_routes',[])
        for cfg in cfgs:
            # module = import_module( cfgs.get('module'))
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
                        print 'registered blueprint route:', path


    def getRouteConfig(self):
        return self.conf.get('blueprint_routes')

    def _checkConfig(self):
        pass

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