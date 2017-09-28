#coding:utf-8

import json
from camel.fundamental.basetype import ValueEntry


YES = 1
NO = 2

class TypeBase(object):
    UNKNOWN = ValueEntry(0, u'')

class ProviderType(TypeBase):
    G7      = ValueEntry(1,u'G7')
    ZJXL    = ValueEntry(2,u'中交兴路')
    YL      = ValueEntry(3,u'易流')
    ZQ      = ValueEntry(4,u'重汽')
    BD      = ValueEntry(5,u'运盟司机App接入百度鹰眼数据')
    KMS     = ValueEntry(6,u'康明斯')
    XR      = ValueEntry(7,u'杭州星软')
    JF      = ValueEntry(8,u'杭州及方')
    HB      = ValueEntry(9,u'深圳华宝')
    KL      = ValueEntry(10,u'上海控络')


"""
|KMS|6|int|康明斯|
|XR|7|int|杭州星软|
|JF|8|int|杭州及方|
|HB|9|int|深圳华宝|
|KL|10|int|上海控络|

"""
# class PayloadType(TypeBase):
#     LOC     = ValueEntry(0x01,u'位置信息')
#     EMS     = ValueEntry(0x02,u'发送机数据')
#     ETC     = ValueEntry(0x04,u'ETC数据')

class LocationDeviceType(TypeBase):
    GPS     = ValueEntry(1,u'GPS定位数据')
    BD      = ValueEntry(2,u'北斗定位数据')

class LocationNeedFix(TypeBase):
    YES = ValueEntry(1,u'yes')
    NO = ValueEntry(2,u'no')

class LocationEncodeType(TypeBase):
    WGS84   = ValueEntry(1,u'GPS')
    GCJ     = ValueEntry(2,u'国测局')
    BD      = ValueEntry(3,u'百度坐标')

class DataCategory(TypeBase):
    LOC = ValueEntry('A', u'位置信息')
    EMS = ValueEntry('B', u'发送机数据')
    ETC = ValueEntry('C', u'ETC数据')

    def __init__(self,moid,type_,version=1,provider = TypeBase.UNKNOWN.value):
        self.type = type_
        self.version = version  # 版本
        self.provider = provider    #供应商
        # self.sys_time = 0       #系统时间
        self.moid = moid

    def getId(self):
        return self.moid

    def unique(self):
        return 0

    def marshall(self):
        return json.dumps(self.dict())

    @classmethod
    def unmarshall(cls,data):
        content = data
        if isinstance(data,str):
            content = json.loads(data)
        obj = None
        if content.get('type') == DataCategory.LOC.value:
            obj = LocationData.unmarshall(content)

        if obj:
            obj.type = content.get('type',TypeBase.UNKNOWN.value)
            obj.version = content.get('version','0')
            obj.provider = content.get('provider',ProviderType.UNKNOWN.value)
            obj.moid = content.get('moid','')
        return obj

    def dict(self):
        obj = self
        attrs = [s for s in dir(obj) if not s.startswith('__')]
        kvs = {}
        for k in attrs:
            attr = getattr(obj, k)
            if not callable(attr) and not isinstance(attr,ValueEntry):
                kvs[k] = attr
        return kvs

    def toEnvelope(self):
        env = DataEnvelope(self.moid,self.provider)
        env.add(self)
        return env

class LocationData(DataCategory):
    """位置数据"""
    def __init__(self,moid='',lon=0.0,lat=0.0,speed=0.0,direction=0.0,
        time=0,altitute=0.0,encode=LocationEncodeType.WGS84.value):
        DataCategory.__init__(self,moid,DataCategory.LOC.value)

        self.lon = lon
        self.lat = lat
        self.speed = speed
        self.direction = direction
        self.time = time
        self.altitute = altitute
        self.encode = encode                        # 位置点编码类型  默认wgs84
        self.need_fix = LocationNeedFix.NO.value    # 无需修正
        self.status = 0
        self.address = ''
        self.text = ''


        self.extra = {

        }

    def unique(self):
        return self.time

    @classmethod
    def unmarshall(cls,data):

        if isinstance(data,str):
            data = json.loads(data)
        obj = cls()
        obj.lon = data.get('lon',0)
        obj.lat = data.get('lat',0)
        obj.speed = data.get('speed',0)
        obj.direction = data.get('direction',0)
        obj.time = data.get('time',0)
        obj.altitude = data.get('altitue',0)
        obj.encode = data.get('encode',LocationEncodeType.UNKNOWN.value)
        obj.need_fix = data.get('need_fix',LocationNeedFix.NO.value)
        obj.extra = data.get('extra',{})
        obj.address = data.get('address','')
        obj.status = data.get('status',0)
        obj.text = data.get('text','')

        return obj


class EMS_Data( DataCategory ):
    """发送机采集数据"""
    def __init__(self,moid):
        DataCategory.__init__(self,moid,DataCategory.EMS)

    def unique(self):
        return 0

class DataEnvelope(object):
    """
    :param version
    :type version float
    :param provider 设备供应商类型
    :type provider DataProviderType
    """
    def __init__(self,id,provider=''):
        self.id = id
        self.provider = provider
        self.payloads={}

    def getId(self):
        return self.id

    # @property
    # def payload_mask(self):
    #     mask = 0
    #     for _ in self.payloads.values():
    #         mask |= _.type
    #     return mask

    def getItem(self,type_):
        return self.payloads.get(type_)

    def getPayloads(self):
        return self.payloads.values()

    def add(self,data):
        self.payloads[data.type] = data
        return self

    def dict(self):
        data = {
            'id': self.id,
            'provider': self.provider,
            'payloads':{},
        }
        for k,v in self.payloads.items():
            data['payloads'][k] = v.dict()
        return data

    def marshall(self):
        return json.dumps(self.dict())

    @classmethod
    def unmarshall(cls,data):
        content = data
        if isinstance(data,str):
            content = json.loads(data)
        env = DataEnvelope('')
        env.id = content.get('id','')
        env.provider = content.get('provider',TypeBase.UNKNOWN.value)
        payloads = content.get('payloads',{})
        for k,v in payloads.items():
            obj = DataCategory.unmarshall(v)
            if obj:
                env.payloads[ k ] =  obj
        return env

    def toMovableObject(self):
        mo = MovableObject(self.id)
        mo.datas.update(self.payloads)
        return mo


class MovableObject(object):
    """对象用于保存最新的监控数据
    :param datas:
    :type datas:dict { PayloadType: DataCategory }
    """
    def __init__(self,mo_id):
        self.id = mo_id
        self.name = ''  #车牌
        self.datas = {} #采集数据 { type: data }
        self.tags ={}

    def getData(self,type_=DataCategory.LOC.value):
        """获取指定类型的监控数据
            :param type_
            :type type_ base.DataCategory
        """
        return self.datas.get(type_)

    def setTag(self,tag,value):
        self.tags[tag] = value

    def getTag(self,tag):
        return self.tags.get(tag)

    def getLocation(self):
        return self.datas.get(DataCategory.LOC.value)

    def getId(self):
        return  self.id

    def update(self,new):
        """

        :param new:
        :type new: DataCategory
        :return:
            数据差异 : YES
            数据一致: NO
        """
        yesno = NO
        if isinstance(new,DataCategory):
            yesno = YES
            old = self.datas.get(new.type)
            if old and old.unique() == new.unique():
                print 'data unique duplicated:',new.unique()
                return NO # same data
            self.datas[new.type] = new


        if isinstance(new,DataEnvelope):
            yesno = NO
            if new.id == self.getId():
                for k,v in new.payloads.items():
                    if self.update(v) == YES:
                        yesno = YES

        if isinstance(new ,MovableObject):
            if self.datas != new.datas:
                yesno = YES
                self.datas.update(new.datas)
        return yesno  # difference data

    def dict(self):
        content = {'id': self.id, 'data': {}}
        for k, v in self.datas.items():
            content['data'][k] = v.dict()
        return content

    def marshall(self):
        content = self.dict()
        return json.dumps(content)

    @classmethod
    def unmarshall(cls,data):
        content = data
        if isinstance(data,str):
            content = json.loads(data)
        id = content.get('id','')
        mo = MovableObject(id)
        for k,v in content.get('data',{}).items():
            obj = DataCategory.unmarshall(v)
            mo.datas[ k ] = obj
        return mo

    def equals(self,other):
        pass

"""
1.为了同时接入大规模数量的车辆数据，根据车牌将车辆hash分割到不同接入分区，
分区服务器在发起并行的查询请求
"""