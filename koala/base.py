#coding:utf-8

__author__ = 'zhangbin'

import base64
import binascii

class _CacheEntryFormat:
    UserWithTGS = 'user_mgws$${}'

    @staticmethod
    def getUserKey(user_id):
        user_id = binascii.b2a_hex(user_id)
        return _CacheEntryFormat.UserWithTGS.format( user_id )

CacheEntryConfig = _CacheEntryFormat

class PlatformType:
    P_UNDEFINED = 0
    P_ANDROID = 1
    P_IOS = 2
    P_DESKTOP = 4
    P_HTML5 = 8


class MessageConfirmValue:
    UNACKED = 0
    ACKED = 1


def USER_ID1(ctx):
    '''
        获取一次消息携带的用户身份编号
    '''
    s = ctx.msg.extra.getValue('__user_id__')
    ids = s.split('#')
    userid = ids[0]
    return int(userid)

def USER_ID2(ctx):
    s = ctx.msg.extra.getValue('__user_id__')
    ids = s.split('#')
    userid = ids[0]
    device_id=None
    if len(ids) >1:
        device_id = ids[1]
    return (int(userid),device_id)

def USER_ID(ctx):
    s = ctx.msg.extra.getValue('__user_id__')
    # return int(s)
    return s


def ID1(s):
    ids = s.split('#')
    userid = ids[0]
    return int(userid)

def ID2(s):
    ids = s.split('#')
    userid = ids[0]
    device_id=None
    if len(ids) >1:
        device_id = ids[1]
    return (int(userid),device_id)



def MakeUserId(userid,device_id):
    return "%s#%s"%(userid,device_id)


def CALL_USER_ID(userid):
    '''
        构造包含用户编号的附加属性
    '''
    return {'__user_id__':str(userid) }