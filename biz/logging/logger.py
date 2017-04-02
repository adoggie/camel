#coding:utf-8

from camel.fundamental.logging.logger import Logger


class CamelLogger(Logger):
    def __init__(self,*args,**kwargs):
        Logger.__init__(self,*args,**kwargs)

    def setTransportTag(self,no):
        #设置运单
        from filter import TransportInvoiceFilter
        self.addTag( '%s:%s'%(TransportInvoiceFilter.TAG,no) )

class FlaskHttpRequestLogger(CamelLogger):
    """将日志中的Tags项关联到 flask的request对象中
    """
    def __init__(self,*args,**kwargs):
        CamelLogger.__init__(self,*args,**kwargs)

    def setTags(self,tags):
        from flask import request
        if type(tags) == str:
            ss = tags.strip()
            if ss:
                tags = ss.split(',')
            else:
                tags = []
        # if type(tags) in (tuple,list):
        request.log_tags = tags
        return self

    def getTags(self):
        from flask import request,g
        if not hasattr(request,'log_tags'):
            request.log_tags = []
        return request.log_tags


