#!/usr/bin/ python
#-*- coding:utf-8 -*-

import tornado.web
from application.controller.baseController import baseController

class TestController(baseController):
    '''
    测试控制器
    '''
    
    #默认action
    def action1(self):
        return {'uri':1} 
    
    def action2(self):
        name = self.get_argument('name', 'world !')
        return {'name':name, 'uri':2} 
    
    
