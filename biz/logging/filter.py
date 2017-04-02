#coding:utf-8

from logging import Filter

class TransportInvoiceFilter(Filter):
    """运单日志消息扫描

    """
    TYPE = 'trans'
    TAG = 'TRANS:'
    def __init__(self,*args,**kwargs):
        Filter.__init__(self,*args,**kwargs)

    def filter(self, record):
        NO = 0
        YES = 1
        if record.tags.find( TransportInvoiceFilter.TAG )!=-1:
            return YES
        return NO


class LogHandlerFilterMixer(object):

    def _initLogHandlerFilters(self,handler,names):
        for name in names:
            if name == TransportInvoiceFilter.TYPE:
                flt = TransportInvoiceFilter()
                handler.addFilter( flt )