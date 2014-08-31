#!/usr/bin/ python
#-*- coding:utf-8 -*-

import os
import base64
import tornado.web

class Dispatcher(tornado.web.RequestHandler):
    '''
    Tornado路由分发类
    '''
    
    index = ''

    def get(self):
        '''
        Doc继承Reuest的get方法
        '''
        self.__render()
    
    def post(self):
        self.__render()
    
    
    def __render(self):
        if self.request.uri == '/':
            self.request.uri = self.index
        
        #获取url里面的uri信息
        uri  = self.request.uri.split('?', 1)[0].split('/')[1:]
        
        if len(uri) < 2:
            url = self.index.split('/')[1:]
        args = uri[2:]
        
        #Controller&Action
        _c = uri[0].capitalize() + 'Controller'
        _a = uri[1]
        
        #import controller
        _tmp = __import__(self.__file(uri[0]), globals(), locals(), [_c], -1)
        _class  = getattr(_tmp, _c)(self)
        _action = getattr(_class, _a)
        
        data = _action(*args)
        
        #exit Request for redirect
        if data == 'redirect':
            return     
        
        if not isinstance(data, dict):
            data = {}
        # Set template file.
        tplFile = None
        
        if '__tpl_file' in data:
            tplFile = '%s.htm' % data['__tpl_file']
        else:
            tplFile = '%s.htm' % uri[1]
        
        #todo cookie
        '''
        if self.get_cookie('__uuid'):
            self.clear_cookie('__uuid')
        '''
            
        #模板路径
        tplDir = os.path.join(os.path.dirname(__file__), '..', 'view')
        data['__tpl_dir']  = tplDir
        data['__tpl_path'] = os.path.join(tplDir, uri[0], tplFile)
        
        if '__layout_off' in data:
            self.render(data['__tpl_path'], data=data)
        else:
            self.render(tplDir + '/layout/default.htm', data=data)
    
    
    def __file(self, name):
        '''
        file-naming conventions 
        @param name: file name
        '''
        return 'application.controller.' + name + 'Controller'
