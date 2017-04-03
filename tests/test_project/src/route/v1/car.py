#coding:utf-8

from flask import Blueprint,request,g
from camel.biz.application.flasksrv import instance,db

from camel.model.log.models import Online

app = Blueprint('zoo',__name__)

@app.route('/car')
def car():
    instance.getLogger().debug('abccc')
    instance.getLogger().addTag('TRANS:A001')
    # print request.values
    do_request()
    return 'i am car!'

def do_request():
    instance.getLogger().debug('xxx')


@app.route('/cat')
def cat():
    instance.getLogger().debug('miao~')
    return 'i am cat!'


@app.route('/online')
def lines():

    line = Online()
    line.get_time = '2017-1-1'
    line.mobile = '13916624477'

    db.session.add(line)
    db.session.commit()

    return 'one online record  be created! <%s>'%line.id