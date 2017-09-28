
# -- coding:utf-8 --

#---------------------------------
#  TCE
#  Tiny Communication Engine
#
#  sw2us.com copyright @2012
#  bin.zhang@sw2us.com / qq:24509826
#---------------------------------

import os,os.path,sys,struct,time,traceback,time
import tcelib as tce

	
class SIDS_t:
	# -- SEQUENCE --
	def __init__(self,array):
		self.ds = array
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds))
		for o in self.ds:
			d = tce.serial_string(o,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			size_,= struct.unpack('!I',d[idx:idx+4])
			idx += 4
			p = 0
			while p < size_:
				v,idx = tce.unserial_string(d,idx)
				self.ds.append(v)
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class Properties_t:
	# -- THIS IS DICTIONARY! --
	def __init__(self,ds={}):
		self.ds = ds
		
	def marshall(self):
		d = '' 
		d += struct.pack('!I',len(self.ds.keys()))
		for k,v in self.ds.items():
			d = tce.serial_string(k,d)
			d = tce.serial_string(v,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			_size,= struct.unpack('!I',d[idx:idx+4])
			p = 0
			idx += 4
			while p < _size:
				x,idx = tce.unserial_string(d,idx)
				y,idx = tce.unserial_string(d,idx)
				self.ds[x] = y
				p+=1
		except:
			traceback.print_exc()
			return False,idx
		return True,idx

class Error_t:
# -- STRUCT -- 
	def __init__(self,succ=False,code=0,msg=""):
		self.succ = succ
		self.code = code
		self.msg = msg
		
	def __str__(self):
		return 'OBJECT<Error_t :%s> { succ:%s,code:%s,msg:%s}'%(hex(id(self)),str(self.succ),str(self.code),str(self.msg) ) 
		
	def marshall(self):
		d =''
		d = tce.serial_bool(self.succ,d)
		d += tce.serial_int(self.code,d)
		d = tce.serial_string(self.msg,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.succ,idx = tce.unserial_bool(d,idx)
			self.code,idx = tce.unserial_int(d,idx)
			self.msg,idx = tce.unserial_string(d,idx)
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class CallReturn_t:
# -- STRUCT -- 
	def __init__(self,error=Error_t(),value="",delta=""):
		self.error = error
		self.value = value
		self.delta = delta
		
	def __str__(self):
		return 'OBJECT<CallReturn_t :%s> { error:%s,value:%s,delta:%s}'%(hex(id(self)),str(self.error),str(self.value),str(self.delta) ) 
		
	def marshall(self):
		d =''
		d += self.error.marshall()
		d = tce.serial_string(self.value,d)
		d = tce.serial_string(self.delta,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.error.unmarshall(d,idx)
			if not r: return False,idx
			self.value,idx = tce.unserial_string(d,idx)
			self.delta,idx = tce.unserial_string(d,idx)
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class AuthToken_t:
# -- STRUCT -- 
	def __init__(self,user_id="",user_name="",login_time=0,expire_time=0,platform_type=0,device_id=""):
		self.user_id = user_id
		self.user_name = user_name
		self.login_time = login_time
		self.expire_time = expire_time
		self.platform_type = platform_type
		self.device_id = device_id
		
	def __str__(self):
		return 'OBJECT<AuthToken_t :%s> { user_id:%s,user_name:%s,login_time:%s,expire_time:%s,platform_type:%s,device_id:%s}'%(hex(id(self)),str(self.user_id),str(self.user_name),str(self.login_time),str(self.expire_time),str(self.platform_type),str(self.device_id) ) 
		
	def marshall(self):
		d =''
		d = tce.serial_string(self.user_id,d)
		d = tce.serial_string(self.user_name,d)
		d = tce.serial_long(self.login_time,d)
		d = tce.serial_long(self.expire_time,d)
		d += tce.serial_int(self.platform_type,d)
		d = tce.serial_string(self.device_id,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.user_id,idx = tce.unserial_string(d,idx)
			self.user_name,idx = tce.unserial_string(d,idx)
			self.login_time,idx = tce.unserial_long(d,idx)
			self.expire_time,idx = tce.unserial_long(d,idx)
			self.platform_type,idx = tce.unserial_int(d,idx)
			self.device_id,idx = tce.unserial_string(d,idx)
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class MessageMeta_t:
# -- STRUCT -- 
	def __init__(self,realm="",seq="",sender="",stime=""):
		self.realm = realm
		self.seq = seq
		self.sender = sender
		self.stime = stime
		
	def __str__(self):
		return 'OBJECT<MessageMeta_t :%s> { realm:%s,seq:%s,sender:%s,stime:%s}'%(hex(id(self)),str(self.realm),str(self.seq),str(self.sender),str(self.stime) ) 
		
	def marshall(self):
		d =''
		d = tce.serial_string(self.realm,d)
		d = tce.serial_string(self.seq,d)
		d = tce.serial_string(self.sender,d)
		d = tce.serial_string(self.stime,d)
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			self.realm,idx = tce.unserial_string(d,idx)
			self.seq,idx = tce.unserial_string(d,idx)
			self.sender,idx = tce.unserial_string(d,idx)
			self.stime,idx = tce.unserial_string(d,idx)
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class Message_t:
# -- STRUCT -- 
	def __init__(self,meta=MessageMeta_t(),title="",content="",props={}):
		self.meta = meta
		self.title = title
		self.content = content
		self.props = props
		
	def __str__(self):
		return 'OBJECT<Message_t :%s> { meta:%s,title:%s,content:%s,props:%s}'%(hex(id(self)),str(self.meta),str(self.title),str(self.content),str(self.props) ) 
		
	def marshall(self):
		d =''
		d += self.meta.marshall()
		d = tce.serial_string(self.title,d)
		d = tce.serial_string(self.content,d)
		container = Properties_t(self.props)
		d += container.marshall()
		return d
		
	def unmarshall(self,d,idx_=0):
		idx = idx_
		try:
			r,idx = self.meta.unmarshall(d,idx)
			if not r: return False,idx
			self.title,idx = tce.unserial_string(d,idx)
			self.content,idx = tce.unserial_string(d,idx)
			self.props = {}
			container = Properties_t(self.props)
			r,idx = container.unmarshall(d,idx)
			if not r: return False,idx
		except:
			traceback.print_exc()
			return False,idx
		return True,idx
		

class ITerminal(tce.RpcServantBase):
	# -- INTERFACE -- 
	def __init__(self):
		tce.RpcServantBase.__init__(self)
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[0] = ITerminal_delegate
	
	def onMessage(self,message,ctx):
		pass
	
	def onError(self,errcode,errmsg,ctx):
		pass
	

class ITerminal_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 0
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = self.onMessage
		self.optlist[1] = self.onError
		
		self.inst = inst
	
	def onMessage(self,ctx):
		tce.log_debug("callin (onMessage)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_message = Message_t()
		r,idx = _p_message.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.onMessage(_p_message,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def onError(self,ctx):
		tce.log_debug("callin (onError)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_errcode,idx = tce.unserial_string(d,idx)
		_p_errmsg,idx = tce.unserial_string(d,idx)
		cr = None
		self.inst.onError(_p_errcode,_p_errmsg,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class ITerminalPrx(tce.RpcProxyBase):
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		tce.RpcProxyBase.__init__(self)
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(ep,af= tce.AF_WRITE | tce.AF_READ):
		ep.open(af)
		conn = ep.impl
		proxy = ITerminalPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITerminalPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = ITerminalPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def onMessage(self,message,timeout=None,extra={}):
		# function index: 7
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 0
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		d_2 += message.marshall()
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def onMessage_async(self,message,async,cookie=None,extra={}):
		# function index: 7
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 0
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		d_3 += message.marshall()
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = ITerminalPrx.onMessage_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def onMessage_asyncparser(m,m2):
		# function index: 7 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def onMessage_oneway(self,message,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 0
			m_1.opidx = 0
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			d_2 += message.marshall()
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onError(self,errcode,errmsg,timeout=None,extra={}):
		# function index: idx_4
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 0
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		d_2 = tce.serial_string(errcode,d_2)
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 = tce.serial_string(errmsg,d_2)
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def onError_async(self,errcode,errmsg,async,cookie=None,extra={}):
		# function index: idx_4
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 0
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		d_3 = tce.serial_string(errcode,d_3)
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 = tce.serial_string(errmsg,d_3)
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = ITerminalPrx.onError_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def onError_asyncparser(m,m2):
		# function index: idx_4 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def onError_oneway(self,errcode,errmsg,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 0
			m_1.opidx = 1
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			d_2 = tce.serial_string(errcode,d_2)
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 = tce.serial_string(errmsg,d_2)
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IUserEventListener(tce.RpcServantBase):
	# -- INTERFACE -- 
	def __init__(self):
		tce.RpcServantBase.__init__(self)
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[1] = IUserEventListener_delegate
	
	def onUserOnline(self,user_id,gws_id,device,ctx):
		pass
	
	def onUserOffline(self,user_id,gws_id,device,ctx):
		pass
	

class IUserEventListener_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 1
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = self.onUserOnline
		self.optlist[1] = self.onUserOffline
		
		self.inst = inst
	
	def onUserOnline(self,ctx):
		tce.log_debug("callin (onUserOnline)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_user_id,idx = tce.unserial_string(d,idx)
		_p_gws_id,idx = tce.unserial_string(d,idx)
		_p_device,idx = tce.unserial_int(d,idx)
		cr = None
		self.inst.onUserOnline(_p_user_id,_p_gws_id,_p_device,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def onUserOffline(self,ctx):
		tce.log_debug("callin (onUserOffline)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_user_id,idx = tce.unserial_string(d,idx)
		_p_gws_id,idx = tce.unserial_string(d,idx)
		_p_device,idx = tce.unserial_int(d,idx)
		cr = None
		self.inst.onUserOffline(_p_user_id,_p_gws_id,_p_device,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class IUserEventListenerPrx(tce.RpcProxyBase):
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		tce.RpcProxyBase.__init__(self)
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(ep,af= tce.AF_WRITE | tce.AF_READ):
		ep.open(af)
		conn = ep.impl
		proxy = IUserEventListenerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IUserEventListenerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IUserEventListenerPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def onUserOnline(self,user_id,gws_id,device,timeout=None,extra={}):
		# function index: 8
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 1
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		d_2 = tce.serial_string(user_id,d_2)
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 = tce.serial_string(gws_id,d_2)
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 += tce.serial_int(device,d_2)
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def onUserOnline_async(self,user_id,gws_id,device,async,cookie=None,extra={}):
		# function index: 8
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 1
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		d_3 = tce.serial_string(user_id,d_3)
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 = tce.serial_string(gws_id,d_3)
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 += tce.serial_int(device,d_3)
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = IUserEventListenerPrx.onUserOnline_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def onUserOnline_asyncparser(m,m2):
		# function index: 8 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def onUserOnline_oneway(self,user_id,gws_id,device,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 1
			m_1.opidx = 0
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			d_2 = tce.serial_string(user_id,d_2)
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 = tce.serial_string(gws_id,d_2)
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 += tce.serial_int(device,d_2)
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def onUserOffline(self,user_id,gws_id,device,timeout=None,extra={}):
		# function index: idx_4
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 1
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		d_2 = tce.serial_string(user_id,d_2)
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 = tce.serial_string(gws_id,d_2)
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 += tce.serial_int(device,d_2)
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def onUserOffline_async(self,user_id,gws_id,device,async,cookie=None,extra={}):
		# function index: idx_4
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 1
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		d_3 = tce.serial_string(user_id,d_3)
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 = tce.serial_string(gws_id,d_3)
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 += tce.serial_int(device,d_3)
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = IUserEventListenerPrx.onUserOffline_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def onUserOffline_asyncparser(m,m2):
		# function index: idx_4 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def onUserOffline_oneway(self,user_id,gws_id,device,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 1
			m_1.opidx = 1
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			d_2 = tce.serial_string(user_id,d_2)
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 = tce.serial_string(gws_id,d_2)
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 += tce.serial_int(device,d_2)
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class ITerminalGatewayServer(tce.RpcServantBase):
	# -- INTERFACE -- 
	def __init__(self):
		tce.RpcServantBase.__init__(self)
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[2] = ITerminalGatewayServer_delegate
	
	def ping(self,ctx):
		pass
	

class ITerminalGatewayServer_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 2
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = self.ping
		
		self.inst = inst
	
	def ping(self,ctx):
		tce.log_debug("callin (ping)")
		d = ctx.msg.paramstream 
		idx = 0
		cr = None
		self.inst.ping(ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class ITerminalGatewayServerPrx(tce.RpcProxyBase):
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		tce.RpcProxyBase.__init__(self)
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(ep,af= tce.AF_WRITE | tce.AF_READ):
		ep.open(af)
		conn = ep.impl
		proxy = ITerminalGatewayServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = ITerminalGatewayServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = ITerminalGatewayServerPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def ping(self,timeout=None,extra={}):
		# function index: 9
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 2
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def ping_async(self,async,cookie=None,extra={}):
		# function index: 9
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 2
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = ITerminalGatewayServerPrx.ping_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def ping_asyncparser(m,m2):
		# function index: 9 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def ping_oneway(self,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 2
			m_1.opidx = 0
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

class IMessageServer(tce.RpcServantBase):
	# -- INTERFACE -- 
	def __init__(self):
		tce.RpcServantBase.__init__(self)
		if not hasattr(self,'delegatecls'):
			self.delegatecls = {}
		self.delegatecls[3] = IMessageServer_delegate
	
	def sendMessage(self,targets,message,ctx):
		pass
	
	def acknowledge(self,seqs,ctx):
		pass
	

class IMessageServer_delegate:
	def __init__(self,inst,adapter,conn=None):
		self.index = 3
		self.optlist={}
		self.id = '' 
		self.adapter = adapter
		self.optlist[0] = self.sendMessage
		self.optlist[1] = self.acknowledge
		
		self.inst = inst
	
	def sendMessage(self,ctx):
		tce.log_debug("callin (sendMessage)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_targets =[] 
		container = SIDS_t(_p_targets)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		_p_message = Message_t()
		r,idx = _p_message.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.sendMessage(_p_targets,_p_message,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	def acknowledge(self,ctx):
		tce.log_debug("callin (acknowledge)")
		d = ctx.msg.paramstream 
		idx = 0
		_p_seqs =[] 
		container = SIDS_t(_p_seqs)
		r,idx = container.unmarshall(d,idx)
		if not r: return False
		cr = None
		self.inst.acknowledge(_p_seqs,ctx)
		if ctx.msg.calltype & tce.RpcMessage.ONEWAY: return True
		d = '' 
		m = tce.RpcMessageReturn(self.inst)
		m.sequence = ctx.msg.sequence
		m.callmsg = ctx.msg
		m.ifidx = ctx.msg.ifidx
		m.call_id = ctx.msg.call_id
		m.conn = ctx.msg.conn
		m.extra = ctx.msg.extra
		if d: m.paramstream += d
		ctx.conn.sendMessage(m)
		return True
	
	
class IMessageServerPrx(tce.RpcProxyBase):
	# -- INTERFACE PROXY -- 
	def __init__(self,conn):
		tce.RpcProxyBase.__init__(self)
		self.conn = conn
		self.delta = None
		pass
	
	@staticmethod
	def create(ep,af= tce.AF_WRITE | tce.AF_READ):
		ep.open(af)
		conn = ep.impl
		proxy = IMessageServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithEpName(name):
		ep = tce.RpcCommunicator.instance().currentServer().findEndPointByName(name)
		if not ep: return None
		conn = ep.impl
		proxy = IMessageServerPrx(conn)
		return proxy
	
	@staticmethod
	def createWithProxy(prx):
		proxy = IMessageServerPrx(prx.conn)
		return proxy
	
	#extra must be map<string,string>
	def sendMessage(self,targets,message,timeout=None,extra={}):
		# function index: 10
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 3
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		container_3 = SIDS_t(targets)
		d_2 += container_3.marshall()
		m_1.paramstream += d_2
		d_2 = '' 
		d_2 += message.marshall()
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def sendMessage_async(self,targets,message,async,cookie=None,extra={}):
		# function index: 10
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 3
		m_1.opidx = 0
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		container_4 = SIDS_t(targets)
		d_3 += container_4.marshall()
		m_1.paramstream += d_3
		d_3 = '' 
		d_3 += message.marshall()
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = IMessageServerPrx.sendMessage_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def sendMessage_asyncparser(m,m2):
		# function index: 10 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def sendMessage_oneway(self,targets,message,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 3
			m_1.opidx = 0
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			container_3 = SIDS_t(targets)
			d_2 += container_3.marshall()
			m_1.paramstream += d_2
			d_2 = '' 
			d_2 += message.marshall()
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	#extra must be map<string,string>
	def acknowledge(self,seqs,timeout=None,extra={}):
		# function index: idx_4
		
		m_1 = tce.RpcMessageCall(self)
		m_1.ifidx = 3
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_2 = '' 
		container_3 = SIDS_t(seqs)
		d_2 += container_3.marshall()
		m_1.paramstream += d_2
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		r_4 = self.conn.sendMessage(m_1)
		if not r_4:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		if not timeout: timeout = tce.RpcCommunicator.instance().getRpcCallTimeout()
		m_5 = None
		try:
			m_5 = m_1.mtx.get(timeout=timeout)
		except:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_TIMEOUT)
		if m_5.errcode != tce.RpcConsts.RPCERROR_SUCC:
			raise tce.RpcException(m_5.errcode)
		m_1 = m_5
	
	def acknowledge_async(self,seqs,async,cookie=None,extra={}):
		# function index: idx_4
		
		ecode_2 = tce.RpcConsts.RPCERROR_SUCC
		m_1 = tce.RpcMessageCall(self)
		m_1.cookie = cookie
		m_1.ifidx = 3
		m_1.opidx = 1
		m_1.extra.setStrDict(extra)
		d_3 = '' 
		container_4 = SIDS_t(seqs)
		d_3 += container_4.marshall()
		m_1.paramstream += d_3
		m_1.prx = self
		m_1.conn = m_1.prx.conn
		m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
		m_1.async = async
		m_1.asyncparser = IMessageServerPrx.acknowledge_asyncparser
		r_5 = self.conn.sendMessage(m_1)
		if not r_5:
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	
	@staticmethod
	def acknowledge_asyncparser(m,m2):
		# function index: idx_4 , m2 - callreturn msg.
		
		stream_1 = m2.paramstream
		user_2 = m.async
		prx_3 = m.prx
		if m2.errcode != tce.RpcConsts.RPCERROR_SUCC: return 
		try:
			idx_4 = 0
			d_5 = stream_1
			r_6 = True
			if r_6:
				user_2(prx_3,m.cookie)
		except:
			traceback.print_exc()
		
	
	def acknowledge_oneway(self,seqs,extra={}):
		# function index: idx_4
		
		try:
			m_1 = tce.RpcMessageCall(self)
			m_1.ifidx = 3
			m_1.opidx = 1
			m_1.calltype |= tce.RpcMessage.ONEWAY
			m_1.prx = self
			m_1.conn = m_1.prx.conn
			m_1.call_id = tce.RpcCommunicator.instance().currentServer().getId()
			m_1.extra.setStrDict(extra)
			d_2 = '' 
			container_3 = SIDS_t(seqs)
			d_2 += container_3.marshall()
			m_1.paramstream += d_2
			r_4 = self.conn.sendMessage(m_1)
			if not r_4:
				raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
		except:
			traceback.print_exc()
			raise tce.RpcException(tce.RpcConsts.RPCERROR_SENDFAILED)
	

