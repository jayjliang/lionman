# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os,json
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker

from ws import RoomHandler
from room import RoomStaticHandler



define("port", default=7000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/room',RoomStaticHandler),
            (r'/ws', RoomHandler),
            (r'/herald/.*', PageNotFoundHandler)
            ]
        settings = dict(
            cookie_secret="8DB90KLP8371B5AEAC5E64C6042415EF",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            # autoload=True,
            # autoescape=None
        )
        tornado.web.Application.__init__(self, handlers,**settings)

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('404.html')
    def post(self):
        self.render('404.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
