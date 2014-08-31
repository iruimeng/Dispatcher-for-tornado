#!/usr/bin/ python
#-*- coding:utf-8 -*-

import base64
import tornado.web


class baseController:
    '''
    doc控制器基类
    '''
    #dispather路由类
    dispatcher = None
    
    #request基础tornado的request变量
    request = None
    
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.request    = self.dispatcher.request
        
    
    #重写request handle的函数方法。可自己重写handler方法添加在此文件。
    def clear_cookie(self, key):
        return self.dispatcher.clear_cookie(key)

    def set_cookie(self, key, message):
        self.set_cookie(key, message)
        return
    
    def get_cookie(self, key):
        return self.dispatcher.get_cookie(key)
    
    def get_argument(self, key, val):
        return self.dispatcher.get_argument(key, val)

    def get_arguments(self, key, val):
        return self.dispatcher.get_arguments(key, val)

    
    def redirect(self, url):
        self.dispatcher.redirect(url)
        return 'redirect'
    
    
    #def __call__(self, ):
    
