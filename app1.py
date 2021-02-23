import os
import pyupbit
import pprint
import dotenv
import time
import json

'''
price = pyupbit.get_current_price(["BTC-XRP", "KRW-XRP"])
print(price)
'''

dotenv.load_dotenv(dotenv_path=".env")

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

upbit = pyupbit.Upbit(access_key, secret_key)
balancies = upbit.get_balances()

markets = [
  "KRW-BTC", "KRW-BTG", "KRW-MTL", "KRW-XEM", "KRW-QTCON"
]

'''
markets = list()
for balance in balancies:
  marekt = "KRW-%s" % ( balance.get("currency") )
  markets.append( marekt )
  
print( markets )
'''

# markets = [ "KRW-%s" % ( balance.get("currency",None) ) for balance in balancies if balance.get("currency") is not None ]

while True:
  orderbook = pyupbit.get_current_price( markets )
  os.system("cls")
  for market in markets:
    print(f'{market:10s}:{orderbook[market]:15,}')
  time.sleep(0.5)

