import pyupbit
import time

from socketio import Namespace
from urllib.parse import urlsplit, parse_qsl 

__all__ = [
  "UpbitNamespace"
]

class UpbitNamespace(Namespace):
  def __init__(self, sio, namespace, *args, **kwargs):
    super(Namespace, self).__init__(namespace, *args, **kwargs)
    
    self.sio = sio
    self.logger = sio.logger

  def on_connect(self, sid, env):
    print("connected", sid)
    params = dict(parse_qsl(urlsplit(env["QUERY_STRING"]).path))
  
  def on_disconnect(self, sid):
    print("disconnect", sid)

  def on_send_price(self, sid, markets):
    self.emit("rcv_price", markets)
