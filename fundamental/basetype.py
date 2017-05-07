#coding:utf-8



class ValueEntry:
    def __init__(self,value,comment=''):
        self.value = value
        self.comment = comment

    def __get__(self, instance, owner):
        return self.value


CAMEL_HOME='/srv/camel'

