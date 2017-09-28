
// -- coding:utf-8 --
//---------------------------------
//  TCE
//  Tiny Communication Engine
//
//  sw2us.com copyright @2012
//  bin.zhang@sw2us.com / qq:24509826
//---------------------------------

	
define("koala",["tce"],function(tce){


function SIDS_thlp(ds){
	//# -- SEQUENCE --
	
	this.ds = ds; // Array()
	
	this.getsize = function(){
		var size =4;
		for(var p=0;p<this.ds.length;p++){
			var _bx_1 =this.ds[p];
			var _sb_2 = tce.utf16to8(_bx_1);
			size+= 4 + _sb_2.getBytes().length;
		}		
		return size;
	}	;	
	
	this.marshall = function(view,pos){
		view.setUint32(pos,this.ds.length);
		pos+=4;
		for(var n=0;n<this.ds.length;n++){
			var _sb_1 = tce.utf16to8(this.ds[n]).getBytes();
			view.setInt32(pos,_sb_1.length);
			pos+=4;
			var _sb_2 = new Uint8Array(view.buffer);
			_sb_2.set(_sb_1,pos);
			pos += _sb_1.length;
		}		
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		var _size_1 = view.getUint32(pos);
		pos+=4;
		for(var _p=0;_p < _size_1;_p++){
			var _o = "";
			var _sb_3 = view.getUint32(pos);
			pos+=4;
			_o = view.buffer.slice(pos,pos+_sb_3);
			// this var is Uint8Array,should convert to String!!
			pos+= _sb_3;
			_o = String.fromCharCode.apply(null, _o.getBytes());
			_o = tce.utf8to16(_o);
			this.ds.push(_o);
		}		
		return pos;
	}	;	
	
}



function Properties_thlp(ds){
	//# -- THIS IS DICTIONARY! --
	this.ds = ds;
	
	
	this.getsize = function(){
		var size =4;
		for(var _k_5 in this.ds){
			var _v_6 = this.ds[_k_5];
			var _sb_7 = tce.utf16to8(_k_5);
			size+= 4 + _sb_7.getBytes().length;
			var _sb_8 = tce.utf16to8(_v_6);
			size+= 4 + _sb_8.getBytes().length;
		}		
		return size;
	}	;	
	
	this.marshall = function(view,pos){
		view.setUint32(pos,Object.keys(this.ds).length);
		pos+=4;
		for( var _k_1 in this.ds){
			var _v_2 = this.ds[_k_1];
			var _sb_3 = tce.utf16to8(_k_1).getBytes();
			view.setInt32(pos,_sb_3.length);
			pos+=4;
			var _sb_4 = new Uint8Array(view.buffer);
			_sb_4.set(_sb_3,pos);
			pos += _sb_3.length;
			var _sb_5 = tce.utf16to8(_v_2).getBytes();
			view.setInt32(pos,_sb_5.length);
			pos+=4;
			var _sb_6 = new Uint8Array(view.buffer);
			_sb_6.set(_sb_5,pos);
			pos += _sb_5.length;
		}		
		return pos;
	}	
	
	// unmarshall()
	this.unmarshall = function(view,pos){
		var _size_1 = 0;
		_size_1 = view.getInt32(pos);
		pos+=4;
		for(var _p=0;_p < _size_1;_p++){
			var _k_2 = "";
			var _sb_5 = view.getUint32(pos);
			pos+=4;
			_k_2 = view.buffer.slice(pos,pos+_sb_5);
			// this var is Uint8Array,should convert to String!!
			pos+= _sb_5;
			_k_2 = String.fromCharCode.apply(null, _k_2.getBytes());
			_k_2 = tce.utf8to16(_k_2);
			var _v_3 = "";
			var _sb_8 = view.getUint32(pos);
			pos+=4;
			_v_3 = view.buffer.slice(pos,pos+_sb_8);
			// this var is Uint8Array,should convert to String!!
			pos+= _sb_8;
			_v_3 = String.fromCharCode.apply(null, _v_3.getBytes());
			_v_3 = tce.utf8to16(_v_3);
			this.ds[_k_2]=_v_3;
		}		
		return pos;
	}	
}
//-- end Dictonary Class definations --




function Error_t(){
// -- STRUCT -- 
	this.succ = false; 
	this.code = 0; 
	this.msg = ""; 
	
	this.getsize = function(){
		var size =0;
		size+= 1;
		size+= 4;
		var _sb_1 = tce.utf16to8(this.msg);
		size+= 4 + _sb_1.getBytes().length;
		return size;
	}	;	
	
	// 
	this.marshall = function(view,pos){
		view.setUint8(pos,this.succ==true?1:0);
		pos+=1;
		view.setInt32(pos,this.code);
		pos+=4;
		var _sb_1 = tce.utf16to8(this.msg).getBytes();
		view.setInt32(pos,_sb_1.length);
		pos+=4;
		var _sb_2 = new Uint8Array(view.buffer);
		_sb_2.set(_sb_1,pos);
		pos += _sb_1.length;
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		var _b_1 = view.getInt8(pos);
		this.succ = _b_1==0?false:true;
		pos+=1;
		this.code = view.getInt32(pos);
		pos+=4;
		var _sb_2 = view.getUint32(pos);
		pos+=4;
		this.msg = view.buffer.slice(pos,pos+_sb_2);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_2;
		this.msg = String.fromCharCode.apply(null, this.msg.getBytes());
		this.msg = tce.utf8to16(this.msg);
		return pos;
	}	;	
	 // --  end function -- 
	
}




function CallReturn_t(){
// -- STRUCT -- 
	this.error = new Error_t(); 
	this.value = ""; 
	this.delta = ""; 
	
	this.getsize = function(){
		var size =0;
		size+=this.error.getsize();
		var _sb_1 = tce.utf16to8(this.value);
		size+= 4 + _sb_1.getBytes().length;
		var _sb_2 = tce.utf16to8(this.delta);
		size+= 4 + _sb_2.getBytes().length;
		return size;
	}	;	
	
	// 
	this.marshall = function(view,pos){
		pos= this.error.marshall(view,pos);
		var _sb_1 = tce.utf16to8(this.value).getBytes();
		view.setInt32(pos,_sb_1.length);
		pos+=4;
		var _sb_2 = new Uint8Array(view.buffer);
		_sb_2.set(_sb_1,pos);
		pos += _sb_1.length;
		var _sb_3 = tce.utf16to8(this.delta).getBytes();
		view.setInt32(pos,_sb_3.length);
		pos+=4;
		var _sb_4 = new Uint8Array(view.buffer);
		_sb_4.set(_sb_3,pos);
		pos += _sb_3.length;
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		pos = this.error.unmarshall(view,pos);
		var _sb_1 = view.getUint32(pos);
		pos+=4;
		this.value = view.buffer.slice(pos,pos+_sb_1);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_1;
		this.value = String.fromCharCode.apply(null, this.value.getBytes());
		this.value = tce.utf8to16(this.value);
		var _sb_3 = view.getUint32(pos);
		pos+=4;
		this.delta = view.buffer.slice(pos,pos+_sb_3);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_3;
		this.delta = String.fromCharCode.apply(null, this.delta.getBytes());
		this.delta = tce.utf8to16(this.delta);
		return pos;
	}	;	
	 // --  end function -- 
	
}




function AuthToken_t(){
// -- STRUCT -- 
	this.user_id = ""; 
	this.user_name = ""; 
	this.login_time = 0; 
	this.expire_time = 0; 
	this.platform_type = 0; 
	this.device_id = ""; 
	
	this.getsize = function(){
		var size =0;
		var _sb_1 = tce.utf16to8(this.user_id);
		size+= 4 + _sb_1.getBytes().length;
		var _sb_2 = tce.utf16to8(this.user_name);
		size+= 4 + _sb_2.getBytes().length;
		size+= 8;
		size+= 8;
		size+= 4;
		var _sb_3 = tce.utf16to8(this.device_id);
		size+= 4 + _sb_3.getBytes().length;
		return size;
	}	;	
	
	// 
	this.marshall = function(view,pos){
		var _sb_1 = tce.utf16to8(this.user_id).getBytes();
		view.setInt32(pos,_sb_1.length);
		pos+=4;
		var _sb_2 = new Uint8Array(view.buffer);
		_sb_2.set(_sb_1,pos);
		pos += _sb_1.length;
		var _sb_3 = tce.utf16to8(this.user_name).getBytes();
		view.setInt32(pos,_sb_3.length);
		pos+=4;
		var _sb_4 = new Uint8Array(view.buffer);
		_sb_4.set(_sb_3,pos);
		pos += _sb_3.length;
		view.setFloat64(pos,this.login_time);
		pos+=8;
		view.setFloat64(pos,this.expire_time);
		pos+=8;
		view.setInt32(pos,this.platform_type);
		pos+=4;
		var _sb_5 = tce.utf16to8(this.device_id).getBytes();
		view.setInt32(pos,_sb_5.length);
		pos+=4;
		var _sb_6 = new Uint8Array(view.buffer);
		_sb_6.set(_sb_5,pos);
		pos += _sb_5.length;
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		var _sb_1 = view.getUint32(pos);
		pos+=4;
		this.user_id = view.buffer.slice(pos,pos+_sb_1);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_1;
		this.user_id = String.fromCharCode.apply(null, this.user_id.getBytes());
		this.user_id = tce.utf8to16(this.user_id);
		var _sb_3 = view.getUint32(pos);
		pos+=4;
		this.user_name = view.buffer.slice(pos,pos+_sb_3);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_3;
		this.user_name = String.fromCharCode.apply(null, this.user_name.getBytes());
		this.user_name = tce.utf8to16(this.user_name);
		this.login_time = view.getFloat64(pos);
		pos+=8;
		this.expire_time = view.getFloat64(pos);
		pos+=8;
		this.platform_type = view.getInt32(pos);
		pos+=4;
		var _sb_5 = view.getUint32(pos);
		pos+=4;
		this.device_id = view.buffer.slice(pos,pos+_sb_5);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_5;
		this.device_id = String.fromCharCode.apply(null, this.device_id.getBytes());
		this.device_id = tce.utf8to16(this.device_id);
		return pos;
	}	;	
	 // --  end function -- 
	
}




function MessageMeta_t(){
// -- STRUCT -- 
	this.realm = ""; 
	this.seq = ""; 
	this.sender = ""; 
	this.stime = ""; 
	
	this.getsize = function(){
		var size =0;
		var _sb_1 = tce.utf16to8(this.realm);
		size+= 4 + _sb_1.getBytes().length;
		var _sb_2 = tce.utf16to8(this.seq);
		size+= 4 + _sb_2.getBytes().length;
		var _sb_3 = tce.utf16to8(this.sender);
		size+= 4 + _sb_3.getBytes().length;
		var _sb_4 = tce.utf16to8(this.stime);
		size+= 4 + _sb_4.getBytes().length;
		return size;
	}	;	
	
	// 
	this.marshall = function(view,pos){
		var _sb_1 = tce.utf16to8(this.realm).getBytes();
		view.setInt32(pos,_sb_1.length);
		pos+=4;
		var _sb_2 = new Uint8Array(view.buffer);
		_sb_2.set(_sb_1,pos);
		pos += _sb_1.length;
		var _sb_3 = tce.utf16to8(this.seq).getBytes();
		view.setInt32(pos,_sb_3.length);
		pos+=4;
		var _sb_4 = new Uint8Array(view.buffer);
		_sb_4.set(_sb_3,pos);
		pos += _sb_3.length;
		var _sb_5 = tce.utf16to8(this.sender).getBytes();
		view.setInt32(pos,_sb_5.length);
		pos+=4;
		var _sb_6 = new Uint8Array(view.buffer);
		_sb_6.set(_sb_5,pos);
		pos += _sb_5.length;
		var _sb_7 = tce.utf16to8(this.stime).getBytes();
		view.setInt32(pos,_sb_7.length);
		pos+=4;
		var _sb_8 = new Uint8Array(view.buffer);
		_sb_8.set(_sb_7,pos);
		pos += _sb_7.length;
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		var _sb_1 = view.getUint32(pos);
		pos+=4;
		this.realm = view.buffer.slice(pos,pos+_sb_1);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_1;
		this.realm = String.fromCharCode.apply(null, this.realm.getBytes());
		this.realm = tce.utf8to16(this.realm);
		var _sb_3 = view.getUint32(pos);
		pos+=4;
		this.seq = view.buffer.slice(pos,pos+_sb_3);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_3;
		this.seq = String.fromCharCode.apply(null, this.seq.getBytes());
		this.seq = tce.utf8to16(this.seq);
		var _sb_5 = view.getUint32(pos);
		pos+=4;
		this.sender = view.buffer.slice(pos,pos+_sb_5);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_5;
		this.sender = String.fromCharCode.apply(null, this.sender.getBytes());
		this.sender = tce.utf8to16(this.sender);
		var _sb_7 = view.getUint32(pos);
		pos+=4;
		this.stime = view.buffer.slice(pos,pos+_sb_7);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_7;
		this.stime = String.fromCharCode.apply(null, this.stime.getBytes());
		this.stime = tce.utf8to16(this.stime);
		return pos;
	}	;	
	 // --  end function -- 
	
}




function Message_t(){
// -- STRUCT -- 
	this.meta = new MessageMeta_t(); 
	this.title = ""; 
	this.content = ""; 
	this.props = {}; 
	
	this.getsize = function(){
		var size =0;
		size+=this.meta.getsize();
		var _sb_1 = tce.utf16to8(this.title);
		size+= 4 + _sb_1.getBytes().length;
		var _sb_2 = tce.utf16to8(this.content);
		size+= 4 + _sb_2.getBytes().length;
		var _b_3 = new Properties_thlp(this.props);
		size+=_b_3.getsize();
		return size;
	}	;	
	
	// 
	this.marshall = function(view,pos){
		pos= this.meta.marshall(view,pos);
		var _sb_1 = tce.utf16to8(this.title).getBytes();
		view.setInt32(pos,_sb_1.length);
		pos+=4;
		var _sb_2 = new Uint8Array(view.buffer);
		_sb_2.set(_sb_1,pos);
		pos += _sb_1.length;
		var _sb_3 = tce.utf16to8(this.content).getBytes();
		view.setInt32(pos,_sb_3.length);
		pos+=4;
		var _sb_4 = new Uint8Array(view.buffer);
		_sb_4.set(_sb_3,pos);
		pos += _sb_3.length;
		var _b_5 = new Properties_thlp(this.props);
		pos = _b_5.marshall(view,pos);
		return pos;
	}	;	
	
	this.unmarshall = function(view,pos){
		pos = this.meta.unmarshall(view,pos);
		var _sb_1 = view.getUint32(pos);
		pos+=4;
		this.title = view.buffer.slice(pos,pos+_sb_1);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_1;
		this.title = String.fromCharCode.apply(null, this.title.getBytes());
		this.title = tce.utf8to16(this.title);
		var _sb_3 = view.getUint32(pos);
		pos+=4;
		this.content = view.buffer.slice(pos,pos+_sb_3);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_3;
		this.content = String.fromCharCode.apply(null, this.content.getBytes());
		this.content = tce.utf8to16(this.content);
		var _b_5 = new Properties_thlp(this.props);
		pos = _b_5.unmarshall(view,pos);
		return pos;
	}	;	
	 // --  end function -- 
	
}



function ITerminalProxy(){
	this.conn = null;
	this.delta =null;
	
	this.destroy = function(){
		try{
			this.conn.close();
		}catch(e){
			tce.RpcCommunicator.instance().getLogger().error(e.toString());
		}		
	}	;	
	
	this.onMessage_oneway = function (message,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 0;
		m.opidx = 0;
		m.paramsize = 1;
		error = arguments[1]?arguments[1]:null;
		m.onerror = error;
		props = arguments[2]?arguments[2]:null;
		m.extra=props;
		try{
			var size =0;
			size+=message.getsize();
			var _bf_6 = new ArrayBuffer(size);
			var _view = new DataView(_bf_6);
			var _pos=0;
			_pos = message.marshall(_view,_pos);
			m.paramstream =_bf_6;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.onMessage_async = function(message,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 0;
		m.opidx		= 0;
		error		= arguments[2]?arguments[2]:null;
		m.onerror	= error;
		props		= arguments[3]?arguments[3]:null;
		m.extra		= props;
		cookie 		= arguments[4]?arguments[4]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 1;
		try{
			var size =0;
			size += message.getsize();
			var _bf_1 = new ArrayBuffer(size);
			var _view = new DataView(_bf_1);
			var _pos=0;
			_pos+=message.marshall(_view,_pos);
			m.paramstream =_bf_1;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.onError_oneway = function (errcode,errmsg,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 0;
		m.opidx = 1;
		m.paramsize = 2;
		error = arguments[2]?arguments[2]:null;
		m.onerror = error;
		props = arguments[3]?arguments[3]:null;
		m.extra=props;
		try{
			var size =0;
			var _sb_2 = tce.utf16to8(errcode);
			size+= 4 + _sb_2.getBytes().length;
			var _sb_3 = tce.utf16to8(errmsg);
			size+= 4 + _sb_3.getBytes().length;
			var _bf_4 = new ArrayBuffer(size);
			var _view = new DataView(_bf_4);
			var _pos=0;
			var _sb_5 = tce.utf16to8(errcode).getBytes();
			_view.setInt32(_pos,_sb_5.length);
			_pos+=4;
			var _sb_6 = new Uint8Array(_view.buffer);
			_sb_6.set(_sb_5,_pos);
			_pos += _sb_5.length;
			var _sb_7 = tce.utf16to8(errmsg).getBytes();
			_view.setInt32(_pos,_sb_7.length);
			_pos+=4;
			var _sb_8 = new Uint8Array(_view.buffer);
			_sb_8.set(_sb_7,_pos);
			_pos += _sb_7.length;
			m.paramstream =_bf_4;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.onError_async = function(errcode,errmsg,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 0;
		m.opidx		= 1;
		error		= arguments[3]?arguments[3]:null;
		m.onerror	= error;
		props		= arguments[4]?arguments[4]:null;
		m.extra		= props;
		cookie 		= arguments[5]?arguments[5]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 2;
		try{
			var size =0;
			var _sb_1 = tce.utf16to8(errcode);
			size+= 4 + _sb_1.getBytes().length;
			var _sb_2 = tce.utf16to8(errmsg);
			size+= 4 + _sb_2.getBytes().length;
			var _bf_3 = new ArrayBuffer(size);
			var _view = new DataView(_bf_3);
			var _pos=0;
			var _sb_4 = tce.utf16to8(errcode).getBytes();
			_view.setInt32(_pos,_sb_4.length);
			_pos+=4;
			var _sb_5 = new Uint8Array(_view.buffer);
			_sb_5.set(_sb_4,_pos);
			_pos += _sb_4.length;
			var _sb_6 = tce.utf16to8(errmsg).getBytes();
			_view.setInt32(_pos,_sb_6.length);
			_pos+=4;
			var _sb_7 = new Uint8Array(_view.buffer);
			_sb_7.set(_sb_6,_pos);
			_pos += _sb_6.length;
			m.paramstream =_bf_3;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.AsyncCallBack = function(m1,m2){
		var array = new Uint8Array(m2.paramstream);
		var view = new DataView(array.buffer);
		var pos=0;
		if(m1.opidx == 0){
			m1.async(m1.prx,m1.cookie);
		}		
		if(m1.opidx == 1){
			m1.async(m1.prx,m1.cookie);
		}		
	}	;	
	
}
ITerminalProxy.create = function(uri){
	var prx = new ITerminalProxy();
	prx.conn = new tce.RpcConnection(uri);
	return prx;
};

ITerminalProxy.createWithProxy = function(proxy){
	var prx = new ITerminalProxy();
	prx.conn = proxy.conn;
	return prx;
};


// class ITerminal
function ITerminal(){
	//# -- INTERFACE -- 
	this.delegate = new ITerminal_delegate(this);
	
	//public  onMessage(message,tce.RpcContext ctx){
	this.onMessage = function(message,ctx){
	}	
	
	//public  onError(errcode,errmsg,tce.RpcContext ctx){
	this.onError = function(errcode,errmsg,ctx){
	}	
}

function ITerminal_delegate(inst) {
	
	this.inst = inst;
	this.ifidx = 0;
	this.invoke = function(m){
		if(m.opidx == 0 ){
			return this.func_0_delegate(m);
		}		
		if(m.opidx == 1 ){
			return this.func_1_delegate(m);
		}		
		return false;
	}	;	
	
	this.func_0_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var message = new Message_t();
		pos= message.unmarshall(view,pos);
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.onMessage(message,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
	this.func_1_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var errcode;
		var _sb_10 = view.getUint32(pos);
		pos+=4;
		errcode = view.buffer.slice(pos,pos+_sb_10);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_10;
		errcode = String.fromCharCode.apply(null, errcode.getBytes());
		errcode = tce.utf8to16(errcode);
		var errmsg;
		var _sb_12 = view.getUint32(pos);
		pos+=4;
		errmsg = view.buffer.slice(pos,pos+_sb_12);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_12;
		errmsg = String.fromCharCode.apply(null, errmsg.getBytes());
		errmsg = tce.utf8to16(errmsg);
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.onError(errcode,errmsg,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
}


function IUserEventListenerProxy(){
	this.conn = null;
	this.delta =null;
	
	this.destroy = function(){
		try{
			this.conn.close();
		}catch(e){
			tce.RpcCommunicator.instance().getLogger().error(e.toString());
		}		
	}	;	
	
	this.onUserOnline_oneway = function (user_id,gws_id,device,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 1;
		m.opidx = 0;
		m.paramsize = 3;
		error = arguments[3]?arguments[3]:null;
		m.onerror = error;
		props = arguments[4]?arguments[4]:null;
		m.extra=props;
		try{
			var size =0;
			var _sb_14 = tce.utf16to8(user_id);
			size+= 4 + _sb_14.getBytes().length;
			var _sb_15 = tce.utf16to8(gws_id);
			size+= 4 + _sb_15.getBytes().length;
			size+= 4;
			var _bf_16 = new ArrayBuffer(size);
			var _view = new DataView(_bf_16);
			var _pos=0;
			var _sb_17 = tce.utf16to8(user_id).getBytes();
			_view.setInt32(_pos,_sb_17.length);
			_pos+=4;
			var _sb_18 = new Uint8Array(_view.buffer);
			_sb_18.set(_sb_17,_pos);
			_pos += _sb_17.length;
			var _sb_19 = tce.utf16to8(gws_id).getBytes();
			_view.setInt32(_pos,_sb_19.length);
			_pos+=4;
			var _sb_20 = new Uint8Array(_view.buffer);
			_sb_20.set(_sb_19,_pos);
			_pos += _sb_19.length;
			_view.setInt32(_pos,device);
			_pos+=4;
			m.paramstream =_bf_16;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.onUserOnline_async = function(user_id,gws_id,device,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 1;
		m.opidx		= 0;
		error		= arguments[4]?arguments[4]:null;
		m.onerror	= error;
		props		= arguments[5]?arguments[5]:null;
		m.extra		= props;
		cookie 		= arguments[6]?arguments[6]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 3;
		try{
			var size =0;
			var _sb_1 = tce.utf16to8(user_id);
			size+= 4 + _sb_1.getBytes().length;
			var _sb_2 = tce.utf16to8(gws_id);
			size+= 4 + _sb_2.getBytes().length;
			size+= 4;
			var _bf_3 = new ArrayBuffer(size);
			var _view = new DataView(_bf_3);
			var _pos=0;
			var _sb_4 = tce.utf16to8(user_id).getBytes();
			_view.setInt32(_pos,_sb_4.length);
			_pos+=4;
			var _sb_5 = new Uint8Array(_view.buffer);
			_sb_5.set(_sb_4,_pos);
			_pos += _sb_4.length;
			var _sb_6 = tce.utf16to8(gws_id).getBytes();
			_view.setInt32(_pos,_sb_6.length);
			_pos+=4;
			var _sb_7 = new Uint8Array(_view.buffer);
			_sb_7.set(_sb_6,_pos);
			_pos += _sb_6.length;
			_view.setInt32(_pos,device);
			_pos+=4;
			m.paramstream =_bf_3;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.onUserOffline_oneway = function (user_id,gws_id,device,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 1;
		m.opidx = 1;
		m.paramsize = 3;
		error = arguments[3]?arguments[3]:null;
		m.onerror = error;
		props = arguments[4]?arguments[4]:null;
		m.extra=props;
		try{
			var size =0;
			var _sb_8 = tce.utf16to8(user_id);
			size+= 4 + _sb_8.getBytes().length;
			var _sb_9 = tce.utf16to8(gws_id);
			size+= 4 + _sb_9.getBytes().length;
			size+= 4;
			var _bf_10 = new ArrayBuffer(size);
			var _view = new DataView(_bf_10);
			var _pos=0;
			var _sb_11 = tce.utf16to8(user_id).getBytes();
			_view.setInt32(_pos,_sb_11.length);
			_pos+=4;
			var _sb_12 = new Uint8Array(_view.buffer);
			_sb_12.set(_sb_11,_pos);
			_pos += _sb_11.length;
			var _sb_13 = tce.utf16to8(gws_id).getBytes();
			_view.setInt32(_pos,_sb_13.length);
			_pos+=4;
			var _sb_14 = new Uint8Array(_view.buffer);
			_sb_14.set(_sb_13,_pos);
			_pos += _sb_13.length;
			_view.setInt32(_pos,device);
			_pos+=4;
			m.paramstream =_bf_10;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.onUserOffline_async = function(user_id,gws_id,device,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 1;
		m.opidx		= 1;
		error		= arguments[4]?arguments[4]:null;
		m.onerror	= error;
		props		= arguments[5]?arguments[5]:null;
		m.extra		= props;
		cookie 		= arguments[6]?arguments[6]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 3;
		try{
			var size =0;
			var _sb_1 = tce.utf16to8(user_id);
			size+= 4 + _sb_1.getBytes().length;
			var _sb_2 = tce.utf16to8(gws_id);
			size+= 4 + _sb_2.getBytes().length;
			size+= 4;
			var _bf_3 = new ArrayBuffer(size);
			var _view = new DataView(_bf_3);
			var _pos=0;
			var _sb_4 = tce.utf16to8(user_id).getBytes();
			_view.setInt32(_pos,_sb_4.length);
			_pos+=4;
			var _sb_5 = new Uint8Array(_view.buffer);
			_sb_5.set(_sb_4,_pos);
			_pos += _sb_4.length;
			var _sb_6 = tce.utf16to8(gws_id).getBytes();
			_view.setInt32(_pos,_sb_6.length);
			_pos+=4;
			var _sb_7 = new Uint8Array(_view.buffer);
			_sb_7.set(_sb_6,_pos);
			_pos += _sb_6.length;
			_view.setInt32(_pos,device);
			_pos+=4;
			m.paramstream =_bf_3;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.AsyncCallBack = function(m1,m2){
		var array = new Uint8Array(m2.paramstream);
		var view = new DataView(array.buffer);
		var pos=0;
		if(m1.opidx == 0){
			m1.async(m1.prx,m1.cookie);
		}		
		if(m1.opidx == 1){
			m1.async(m1.prx,m1.cookie);
		}		
	}	;	
	
}
IUserEventListenerProxy.create = function(uri){
	var prx = new IUserEventListenerProxy();
	prx.conn = new tce.RpcConnection(uri);
	return prx;
};

IUserEventListenerProxy.createWithProxy = function(proxy){
	var prx = new IUserEventListenerProxy();
	prx.conn = proxy.conn;
	return prx;
};


// class IUserEventListener
function IUserEventListener(){
	//# -- INTERFACE -- 
	this.delegate = new IUserEventListener_delegate(this);
	
	//public  onUserOnline(user_id,gws_id,device,tce.RpcContext ctx){
	this.onUserOnline = function(user_id,gws_id,device,ctx){
	}	
	
	//public  onUserOffline(user_id,gws_id,device,tce.RpcContext ctx){
	this.onUserOffline = function(user_id,gws_id,device,ctx){
	}	
}

function IUserEventListener_delegate(inst) {
	
	this.inst = inst;
	this.ifidx = 1;
	this.invoke = function(m){
		if(m.opidx == 0 ){
			return this.func_0_delegate(m);
		}		
		if(m.opidx == 1 ){
			return this.func_1_delegate(m);
		}		
		return false;
	}	;	
	
	this.func_0_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var user_id;
		var _sb_10 = view.getUint32(pos);
		pos+=4;
		user_id = view.buffer.slice(pos,pos+_sb_10);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_10;
		user_id = String.fromCharCode.apply(null, user_id.getBytes());
		user_id = tce.utf8to16(user_id);
		var gws_id;
		var _sb_12 = view.getUint32(pos);
		pos+=4;
		gws_id = view.buffer.slice(pos,pos+_sb_12);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_12;
		gws_id = String.fromCharCode.apply(null, gws_id.getBytes());
		gws_id = tce.utf8to16(gws_id);
		var device;
		device = view.getInt32(pos);
		pos+=4;
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.onUserOnline(user_id,gws_id,device,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
	this.func_1_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var user_id;
		var _sb_14 = view.getUint32(pos);
		pos+=4;
		user_id = view.buffer.slice(pos,pos+_sb_14);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_14;
		user_id = String.fromCharCode.apply(null, user_id.getBytes());
		user_id = tce.utf8to16(user_id);
		var gws_id;
		var _sb_16 = view.getUint32(pos);
		pos+=4;
		gws_id = view.buffer.slice(pos,pos+_sb_16);
		// this var is Uint8Array,should convert to String!!
		pos+= _sb_16;
		gws_id = String.fromCharCode.apply(null, gws_id.getBytes());
		gws_id = tce.utf8to16(gws_id);
		var device;
		device = view.getInt32(pos);
		pos+=4;
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.onUserOffline(user_id,gws_id,device,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
}


function ITerminalGatewayServerProxy(){
	this.conn = null;
	this.delta =null;
	
	this.destroy = function(){
		try{
			this.conn.close();
		}catch(e){
			tce.RpcCommunicator.instance().getLogger().error(e.toString());
		}		
	}	;	
	
	this.ping_oneway = function (error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 2;
		m.opidx = 0;
		m.paramsize = 0;
		error = arguments[0]?arguments[0]:null;
		m.onerror = error;
		props = arguments[1]?arguments[1]:null;
		m.extra=props;
		try{
			var size =0;
			var _bf_18 = new ArrayBuffer(size);
			var _view = new DataView(_bf_18);
			var _pos=0;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.ping_async = function(async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 2;
		m.opidx		= 0;
		error		= arguments[1]?arguments[1]:null;
		m.onerror	= error;
		props		= arguments[2]?arguments[2]:null;
		m.extra		= props;
		cookie 		= arguments[3]?arguments[3]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 0;
		try{
			var size =0;
			var _bf_1 = new ArrayBuffer(size);
			var _view = new DataView(_bf_1);
			var _pos=0;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.AsyncCallBack = function(m1,m2){
		var array = new Uint8Array(m2.paramstream);
		var view = new DataView(array.buffer);
		var pos=0;
		if(m1.opidx == 0){
			m1.async(m1.prx,m1.cookie);
		}		
	}	;	
	
}
ITerminalGatewayServerProxy.create = function(uri){
	var prx = new ITerminalGatewayServerProxy();
	prx.conn = new tce.RpcConnection(uri);
	return prx;
};

ITerminalGatewayServerProxy.createWithProxy = function(proxy){
	var prx = new ITerminalGatewayServerProxy();
	prx.conn = proxy.conn;
	return prx;
};


// class ITerminalGatewayServer
function ITerminalGatewayServer(){
	//# -- INTERFACE -- 
	this.delegate = new ITerminalGatewayServer_delegate(this);
	
	//public  ping(tce.RpcContext ctx){
	this.ping = function(ctx){
	}	
}

function ITerminalGatewayServer_delegate(inst) {
	
	this.inst = inst;
	this.ifidx = 2;
	this.invoke = function(m){
		if(m.opidx == 0 ){
			return this.func_0_delegate(m);
		}		
		return false;
	}	;	
	
	this.func_0_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.ping(ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
}


function IMessageServerProxy(){
	this.conn = null;
	this.delta =null;
	
	this.destroy = function(){
		try{
			this.conn.close();
		}catch(e){
			tce.RpcCommunicator.instance().getLogger().error(e.toString());
		}		
	}	;	
	
	this.sendMessage_oneway = function (targets,message,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 3;
		m.opidx = 0;
		m.paramsize = 2;
		error = arguments[2]?arguments[2]:null;
		m.onerror = error;
		props = arguments[3]?arguments[3]:null;
		m.extra=props;
		try{
			var size =0;
			var _c_3 = new SIDS_thlp(targets);
			size+=_c_3.getsize();
			size+=message.getsize();
			var _bf_4 = new ArrayBuffer(size);
			var _view = new DataView(_bf_4);
			var _pos=0;
			var _c_5 = new SIDS_thlp(targets);
			_pos = _c_5.marshall(_view,_pos);
			_pos = message.marshall(_view,_pos);
			m.paramstream =_bf_4;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.sendMessage_async = function(targets,message,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 3;
		m.opidx		= 0;
		error		= arguments[3]?arguments[3]:null;
		m.onerror	= error;
		props		= arguments[4]?arguments[4]:null;
		m.extra		= props;
		cookie 		= arguments[5]?arguments[5]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 2;
		try{
			var size =0;
			var _c_1 = new SIDS_thlp(targets);
			size += _c_1.getsize();
			size += message.getsize();
			var _bf_2 = new ArrayBuffer(size);
			var _view = new DataView(_bf_2);
			var _pos=0;
			var _c_3 = new SIDS_thlp(targets);
			_pos+=_c_3.marshall(_view,_pos);
			_pos+=message.marshall(_view,_pos);
			m.paramstream =_bf_2;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.acknowledge_oneway = function (seqs,error,props){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ONEWAY);
		m.ifidx = 3;
		m.opidx = 1;
		m.paramsize = 1;
		error = arguments[1]?arguments[1]:null;
		m.onerror = error;
		props = arguments[2]?arguments[2]:null;
		m.extra=props;
		try{
			var size =0;
			var _c_4 = new SIDS_thlp(seqs);
			size+=_c_4.getsize();
			var _bf_5 = new ArrayBuffer(size);
			var _view = new DataView(_bf_5);
			var _pos=0;
			var _c_6 = new SIDS_thlp(seqs);
			_pos = _c_6.marshall(_view,_pos);
			m.paramstream =_bf_5;
			m.prx = this;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "RPCERROR_SENDFAILED";
		}		
	}	;	
	
	this.acknowledge_async = function(seqs,async,error,props,cookie){
		var r = false;
		var m = new tce.RpcMessage(tce.RpcMessage.CALL|tce.RpcMessage.ASYNC);
		m.ifidx		= 3;
		m.opidx		= 1;
		error		= arguments[2]?arguments[2]:null;
		m.onerror	= error;
		props		= arguments[3]?arguments[3]:null;
		m.extra		= props;
		cookie 		= arguments[4]?arguments[4]:null;
		m.cookie	= cookie;
		m.extra		= props;
		m.paramsize = 1;
		try{
			var size =0;
			var _c_1 = new SIDS_thlp(seqs);
			size += _c_1.getsize();
			var _bf_2 = new ArrayBuffer(size);
			var _view = new DataView(_bf_2);
			var _pos=0;
			var _c_3 = new SIDS_thlp(seqs);
			_pos+=_c_3.marshall(_view,_pos);
			m.paramstream =_bf_2;
			m.prx = this;
			m.async = async;
		}catch(e){
			console.log(e.toString());
			throw "RPCERROR_DATADIRTY";
		}		
		r = this.conn.sendMessage(m);
		if(!r){
			throw "tce.RpcConsts.RPCERROR_SENDFAILED";
		}		
	}	;	
	
	
	this.AsyncCallBack = function(m1,m2){
		var array = new Uint8Array(m2.paramstream);
		var view = new DataView(array.buffer);
		var pos=0;
		if(m1.opidx == 0){
			m1.async(m1.prx,m1.cookie);
		}		
		if(m1.opidx == 1){
			m1.async(m1.prx,m1.cookie);
		}		
	}	;	
	
}
IMessageServerProxy.create = function(uri){
	var prx = new IMessageServerProxy();
	prx.conn = new tce.RpcConnection(uri);
	return prx;
};

IMessageServerProxy.createWithProxy = function(proxy){
	var prx = new IMessageServerProxy();
	prx.conn = proxy.conn;
	return prx;
};


// class IMessageServer
function IMessageServer(){
	//# -- INTERFACE -- 
	this.delegate = new IMessageServer_delegate(this);
	
	//public  sendMessage(targets,message,tce.RpcContext ctx){
	this.sendMessage = function(targets,message,ctx){
	}	
	
	//public  acknowledge(seqs,tce.RpcContext ctx){
	this.acknowledge = function(seqs,ctx){
	}	
}

function IMessageServer_delegate(inst) {
	
	this.inst = inst;
	this.ifidx = 3;
	this.invoke = function(m){
		if(m.opidx == 0 ){
			return this.func_0_delegate(m);
		}		
		if(m.opidx == 1 ){
			return this.func_1_delegate(m);
		}		
		return false;
	}	;	
	
	this.func_0_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var targets = [];
		var _array_6 = new SIDS_thlp(targets);
		pos=_array_6.unmarshall(view,pos);
		var message = new Message_t();
		pos= message.unmarshall(view,pos);
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.sendMessage(targets,message,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
	this.func_1_delegate = function(m){
		var r = false;
		var pos =0;
		var array = null;
		var view = null;
		array = new Uint8Array(m.paramstream);
		view = new DataView(array.buffer);
		var seqs = [];
		var _array_7 = new SIDS_thlp(seqs);
		pos=_array_7.unmarshall(view,pos);
		var servant = this.inst;
		var ctx = new tce.RpcContext();
		ctx.msg = m;
		servant.acknowledge(seqs,ctx);
		if( (m.calltype & tce.RpcMessage.ONEWAY) !=0 ){
			return true;
		}		
		
		return r;
	}	;	
	
}

return {
	ITerminal : ITerminal,
	ITerminalProxy : ITerminalProxy	,	
	IUserEventListener : IUserEventListener,
	IUserEventListenerProxy : IUserEventListenerProxy	,	
	ITerminalGatewayServer : ITerminalGatewayServer,
	ITerminalGatewayServerProxy : ITerminalGatewayServerProxy	,	
	IMessageServer : IMessageServer,
	IMessageServerProxy : IMessageServerProxy	
};

});
