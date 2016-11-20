# -*- coding: utf-8 -*-
#!/usr/bin/env python

# @Date    : 2016-05-13 11:20:05
# @Author  : jerry.liangj@qq.com

import json
import datetime
from tornado import websocket

class RoomHandler(websocket.WebSocketHandler):
    clients = set()
    admin_ip = []
    deny_ip = []
   
    @staticmethod
    def send_to_all(message):
      for c in RoomHandler.clients:
          c.write_message(json.dumps(message))

    def open(self):
        # print self,"open"
        RoomHandler.clients.add(self)
        ret = {
            'type':'info',
            'number':len(RoomHandler.clients)
        }
        RoomHandler.send_to_all(ret)
        
            # print str(e)
        # self.write_message(json.dumps(ret))
        # self.stream.set_nodelay(True)
    def admin_message(self,message):
        ret = {
            'type':'admin',
            'message':message,
            'time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        RoomHandler.send_to_all(ret)
    def on_message(self, message):
        try:
            message = json.loads(message)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            remote_ip = self.request.remote_ip
            # if remote_ip in RoomHandler.admin_ip:
            #     self.admin_message(message['content'])
            if remote_ip in RoomHandler.deny_ip:
                pass
                #self.(u"您已被禁言")
            else:
                ret = {
                    'type':'user',
                    'name':message['user'],
                    'message':message['content'],
                    'time':now,
                }
                RoomHandler.send_to_all(ret)
        except Exception,e:
            pass
            # print str(e)

        # self.close()

    def on_close(self):
        # print self,"closed"
        RoomHandler.clients.remove(self)
        ret = {
            'type':'info',
            'number':len(RoomHandler.clients)
        }
        RoomHandler.send_to_all(ret)