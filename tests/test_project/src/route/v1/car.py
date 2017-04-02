#coding:utf-8

from flask import Blueprint,request,g
from camel.biz.application.flasksrv import instance

app = Blueprint('zoo',__name__)

@app.route('/car')
def car():

    instance.getLogger().debug('abccc')
    instance.getLogger().setTransportTag('A001')
    print request.values
    do_request()
    return 'i am car!'

def do_request():
    instance.getLogger().debug('xxx')


@app.route('/cat')
def cat():
    instance.getLogger().debug('miao~')
    return 'i am cat!'