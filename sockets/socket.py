from socketio import Server
from .namespaces import UpbitNamespace

def create_sio():
  sio = Server(async_mode="threading")
  sio.register_namespace(UpbitNamespace(sio, '/upbit'))
  
  return sio
  