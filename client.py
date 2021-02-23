import os
import time
import dotenv
import pyupbit
from socketio import Client, ClientNamespace

print("run: ", os.getpid() )

dotenv.load_dotenv(dotenv_path=".env")

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

class UpbitClientNamespace(ClientNamespace):
  def __init__(self, namespace, *args, **kwargs):
    super(ClientNamespace, self).__init__(namespace, *args, **kwargs)

  def on_connect(self):
    print('on_connect')

  def on_disconnect(self):
    print('on_disconnect')
    
  def get_current_price(self):
    tickers = pyupbit.get_tickers(fiat="KRW")
    
    while True:
      markets = pyupbit.get_current_price( tickers )
      client.emit("send_price", dict(
        tickers=tickers,
        markets=markets,
        size=len(markets)
      ))
      time.sleep(1)

client = UpbitClientNamespace('/upbit')

sio = Client()
sio.register_namespace(client)
sio.connect('http://localhost:3000', namespaces=['/upbit'])

sio.start_background_task(client.get_current_price)

print( sio.connected )
print( sio.connection_namespaces )

try:
  sio.wait()
except KeyboardInterrupt as e:
  if sio.connected:
    sio.disconnect()
