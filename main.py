#!/usr/bin/ python
#-*- coding:utf-8 -*-

import os
import tornado.web
import tornado.ioloop

from application.libs.dispatcher import Dispatcher


settings = {
    "debug":True,
    "static_path": os.path.join(os.path.dirname(__file__), "application", "webroot"),
    "cookie_secret": "901a464399b62ce3026706d249bedb90",
    "xsrf_cookies": True,
}

#default uri for dispatcher
Dispatcher.index = '/test/action1'

application = tornado.web.Application([
    (r'/favicon\.ico', tornado.web.StaticFileHandler, {'path': ''}),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': ''}),
    (r"/.*", Dispatcher),
], **settings)

if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
