#coding:utf-8

from camel.fundamental.basetype import ValueEntry

class ErrorDefs(object):
    SUCC = ValueEntry(0,'success')
    ApplicationNotExisted = ValueEntry(1001,u'应用未注册')
    TicketInvalid = ValueEntry(1004,u'访问令牌错误')
    UserTokenSessionExpired = ValueEntry(1005,u'访问会话过期')
    SystemError = (2001, u'系统错误')
    RejectAddressRestricted = ValueEntry(4001, u'消息推送禁止(发送者地址受限)')
    UserAnotherPlaceLogin = ValueEntry(4002, u'未登录或会话过期')

