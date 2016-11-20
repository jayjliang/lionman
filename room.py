# -*- coding: utf-8 -*-                                                                       
#!/usr/bin/env python                                                                         
                                                                                              
# @Date    : 2016-05-13 11:20:05                                                              
# @Author  : jerry.liangj@qq.com                                                              
                                                                                              
import tornado.web                                                                            
import tornado.gen                                                                            
                                                                                              
class RoomStaticHandler(tornado.web.RequestHandler):                                       
                                                                                              
    def get(self):                                                                                                                                                   
        self.render("room.html")   