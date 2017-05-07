#coding:utf-8

from camel.fundamental.errors import ValueEntry,ErrorEntry

class ErrorDefs(object):
    Succ = ErrorEntry(0,u'成功')
    ParameterIllegal = ErrorEntry(1001,u'参数不完整或数据内容损坏')
    ObjectNotExisted = ErrorEntry(1002,u'目标对象不存在')
    AccessDenied = ErrorEntry(1003,u'无权限操作')
    TokenInvalid = ErrorEntry(1004,u'令牌错误')
    SessionInvalid = ErrorEntry(1005, u'会话错误')
    UserOrPasswordError = ErrorEntry(1006,u'用户账号或密码错误')
    ApplicationAuthorizeError = ErrorEntry(1007,u'应用授权错误')
    SystemError = ErrorEntry(2001,u'系统内部运行故障')
    SystemBusy = ErrorEntry(2002,u'系统忙')



