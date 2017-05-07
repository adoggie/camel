#coding:utf-8

# 生成访问用户token

import uuid
import json
import hashlib
import base64
import time

def encode_user_token(user_info,req_type='tracer'):
    m = hashlib.md5()
    user_info['time'] = int(time.time())
    data = json.dumps(user_info)
    data = base64.b64encode(data)
    return data


def decode_user_token(token):
    data = base64.b64decode(token)
    data = json.loads(data)
    return data