#coding:utf-8


import getopt
import os
import sys
import os.path

from camel.fundamental.utils.useful import Instance,Singleton
from camel.fundamental.basetype import CAMEL_HOME
from camel.fundamental.logging.logger import Logger
from camel.fundamental.parser.yamlparser import YamlConfigParser
from camel.fundamental.logging.filter import LogHandlerFilter

instance = Instance()

class Application(Singleton,object):
    inst = None
    def __init__(self,name=''):
        self.name = name
        self.conf = {}
        self.caches = None
        self.logger = Logger(__name__)
        self.db = None
        self.config_file ='settings.yaml'
        self.log_filters = {}


        global instance
        instance.set(self)

    @property
    def appName(self):
        if not self.name:
            return '<APP_NAME>'
        return self.name

    def getDefaultConfigFile(self):
        return os.path.join(self.getConfigPath(),self.config_file )

    def getHomePath(self):
        # path = os.path.join(self.getCamelHomePath(), 'products', self.name)
        # if not os.path.exists(path):
        #     return os.path.dirname(os.path.abspath(__file__))
        return os.path.join(self.getCamelHomePath(), 'products', self.name)

    def getConfigPath(self):
        return os.path.join( self.getCamelHomePath(),'etc',self.name)

    def getDataPath(self):
        return os.path.join(self.getCamelHomePath(), 'data', self.name)

    def getTempPath(self):
        return os.path.join(self.getCamelHomePath(), 'temp', self.name)

    def getLogPath(self):
        return os.path.join(self.getCamelHomePath(), 'logs', self.name)

    def getRunPath(self):
        return os.path.join(self.getCamelHomePath(), 'run', self.name)

    def getLogger(self):
        return self.logger

    def getCamelHomePath(self):
        path = os.getenv('CAMEL_HOME')
        if path:
            return path
        return CAMEL_HOME


    def getConfig(self):
        return self.conf

    def usage(self):
        pass

    def _initOptions(self):
        """从环境变量 APP_NAME 拾取appname
           从命令行 --name 参数拾取appname
        :return:
        """
        if self.name:
            return
        self.name = os.getenv('APP_NAME')
        options, args = getopt.getopt(sys.argv[1:], 'hc:n:', ['help', 'name=','config=']) # : 带参数
        for name, value in options:
            if name in ['-h', "--help"]:
                self.usage()
                sys.exit()
            if name in ('-n', '--name'):
                self.name = value
            if name in ('-c','--config'):
                self.config_file = name

        if not self.name:
            self.name = ''

    def _initDirectories(self):
        from distutils.dir_util import mkpath
        mkpath(self.getConfigPath())
        mkpath(self.getDataPath())
        mkpath(self.getLogPath())
        mkpath(self.getRunPath())

    def init(self):
        self._init_before()

        self._initOptions()
        self._initDirectories()
        self._initConfig()
        self._initLogs()
        self._initDatabase()
        self._initRPC()
        self._initNoSQL()
        self._initCache()

        self._init_after()

    def _init_before(self):
        pass

    def _init_after(self):
        pass

    def _initConfig(self):
        yaml = self.getDefaultConfigFile()
        self.conf = YamlConfigParser(yaml).props
        self._checkConfig()

    def _checkConfig(self):
        """检查配置项是否okay"""
        pass

    def getDatabase(self):
        return self.db

    def _initDatabase(self):
        pass

    def _initLogger(self):
        return Logger(self.appName)

    def _initLogs(self):
        import logging,string

        ver = self.conf.get('project_version')
        project = self.conf.get('project_name')
        app_id = self.appName
        self.logger = self._initLogger()

        log = self.conf.get('logging')
        level = log.get('level','INFO')
        self.logger.setLevel(level) # 不能设置全局，否则会默认输出到console

        extra = {'project_name':project,'project_version':ver,'app_id':app_id,'tags':''}
        formatter = logging.Formatter(log.get('format'))
        self.logger.setFormat(log.get('format')).setFormatExtra(extra)

        self.logger.setMessageFormat(log.get('message_format'))

        self._initLogHandlerFilters(log.get('filters',{}))

        handlers = log.get('handlers',[])
        for cfg in handlers:
            handler = self._initLogHandler(cfg)
            if handler:
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)


                ss = cfg.get('filter', '').strip()
                if ss:
                    ss = map( string.strip ,ss.split(',') )

                    for s in ss:
                        flt = self.log_filters.get(s)
                        if flt:
                            handler.addFilter(flt)
                        else:
                            print 'error: filter<%s> not found!'%s


    def _initLogHandlerFilters(self,cfgs):
        filters = {}
        for name,cfg in cfgs.items():
            flt = LogHandlerFilter(name,cfg)
            filters[name] = flt
        self.log_filters = filters

    def _initLogHandler(self,cfg):
        """日志handler初始化
        目前仅支持: file(RotatingFileHandler) , console(StreamHandler)

        :param cfg:
        :return:
        """
        from camel.fundamental.logging.handler import  LogFileHandler,LogConsoleHandler

        handler = None
        if cfg.get('type','').lower() == LogFileHandler.TYPE and cfg.get('enable', False) == True:
            logfile = os.path.join(self.getLogPath(), cfg.get('filename'))
            handler = LogFileHandler(logfile, encoding=cfg.get('encoding'), maxBytes=cfg.get('max_bytes'),
                backupCount=cfg.get('backup_count'))

        if cfg.get('type').lower() == LogConsoleHandler.TYPE and cfg.get('enable', False) == True:
            handler = LogConsoleHandler()

        return handler

    def _initNoSQL(self):

        pass

    def _initCache(self):
        from camel.fundamental.cache.manager import CacheManager
        self.caches = CacheManager().loads(self.getConfig().get('caches'))

    def _initRPC(self):
        pass

    def run(self):
        print 'Service [%s] Started..'%self.name

__all__=(instance,Application)



