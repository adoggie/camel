#coding:utf-8

import os
import string
import logging


def __FILE__():
    import inspect
    f = inspect.currentframe().f_back.f_back.f_back
    return f.f_code.co_filename,f.f_lineno

class Logger:
    def __init__(self,name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.fmt_extra = {}
        self.tags = []
        self.level = logging.INFO

    def setLevel(self,level='INFO'):
        maps = {
            'DEBUG':logging.DEBUG,
            'INFO':logging.INFO,
            'WARNING':logging.WARNING,
            'ERROR':logging.ERROR,
            'CRITICAL':logging.CRITICAL
        }
        level = string.upper(level)
        intval = maps.get(level,logging.INFO)
        self.logger.setLevel( intval )
        self.level = intval

    def addHandler(self,handler):
        self.logger.addHandler(handler)
        handler.setLogger(self)
        # handler.setLevel(self.level)

    TEMPLATE_FORMAT = '[%(project_name)s:%(project_version)s %(app_id)s] %(levelname)s %(asctime)s %(filename)s:%(lineno)d [%(tags)s] %(message)s'

    def setFormat(self,fmt = TEMPLATE_FORMAT):
        logging.basicConfig(format= fmt )
        return self

    def setFormatExtra(self,extra):
        self.fmt_extra = extra
        return self


    def setTags(self,tags):
        if type(tags) == str:
            ss = tags.strip()
            if ss:
                tags = ss.split(',')
            else:
                tags = []
        # if type(tags) in (tuple,list):
        self.tags = tags
        return self

    def getTags(self):
        return self.tags

    def addTag(self,tag):
        if self.getTags().count(tag) == 0:
            self.getTags().append(tag)
        return self

    def removeTag(self,tag):
        try:
            self.getTags().remove( tag )
        except:pass


    def _normalize_tags(self,tags):
        ss = ''

        if type(tags) in (tuple, list):
            # tags += self.tags
            tags += self.getTags()
            ss = string.join(map(str, tags), ',')

        if type(tags) == str:
            ss = tags.strip()
            tags=[]
            if ss:
                tags = ss.split(',')
            # tags += self.tags
            tags += self.getTags()
            ss = string.join( map(str,tags),',')
        ss = ss.replace(' ', '_')
        return ss



    def log(self,level,*args,**kwargs):
        """

        :param level:
        :param args:
        :param kwargs:
            tags - list ['HOP','TRANS:A10021']
                - string 'HOP,TRANS:A10021'
        :return:
        """
        extra = self.fmt_extra.copy()

        if kwargs.has_key('tags'):
            extra['tags'] = self._normalize_tags( kwargs['tags'])
        else:
            extra['tags'] = self._normalize_tags('')

        filename,lineno = __FILE__()

        extra['_filename'] = os.path.basename(filename)
        extra['_lineno'] = lineno
        self.logger.log( level , *args,extra = extra )


    def debug(self,*args,**kwargs):
        self.log(logging.DEBUG,*args,**kwargs)
        return self

    def warning(self,*args,**kwargs):
        self.log(logging.WARNING, *args, **kwargs)
        return self

    def critical(self,*args,**kwargs):
        self.log(logging.CRITICAL, *args, **kwargs)
        return self

    def info(self,*args,**kwargs):
        self.log(logging.INFO, *args, **kwargs)
        return self

    def error(self,*args,**kwargs):
        self.log(logging.ERROR, *args, **kwargs)
        return self

