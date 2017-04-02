#coding:utf-8


from flask import Flask,request

from camel.biz.application.flasksrv import FlaskService


import route.v1

class MyService(FlaskService):
    def __init__(self):
        FlaskService.__init__(self)

    def getRouteConfig(self):
        return [ route.v1 ]

MyService().instance().run()

