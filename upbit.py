'''
import jwt   # PyJWT 
import uuid

payload = {
    'access_key': 'uU4RI6nFVNFE2OTs9YwxDj6ebkmZZUXMAsJjHwP0',
    'nonce': str(uuid.uuid4()),
}

#Access Key
#uU4RI6nFVNFE2OTs9YwxDj6ebkmZZUXMAsJjHwP0
#Secret Key
#A8bp7J9DWZWpJIgu00yDdTjBtnA7f8QRKkLANxWF

jwt_token = jwt.encode(payload, 'A8bp7J9DWZWpJIgu00yDdTjBtnA7f8QRKkLANxWF',).decode('utf8')
authorization_token = 'Bearer {}'.format(jwt_token)
'''

'''
import requests

url = "https://api.upbit.com/v1/market/all"

querystring = {
  "isDetails":"false"
}

response = requests.request("GET", url, params=querystring)

print(response.text)
'''

'''
import requests
import pprint
import json

url = "https://api.upbit.com/v1/candles/days"
querystring = {
  "count": "1",
  "market": "KRW-BTC"
}

response = requests.request("GET", url, params=querystring)

pprint.pprint(json.loads(response.text))
'''

'''
import requests
import pprint
import json

url = "https://api.upbit.com/v1/ticker"
querystring = {
  "count": "1",
  "markets": "KRW-BTC,KRW-BTG,KRW-MTL,KRW-XEM"
}

response = requests.request("GET", url, params=querystring)

pprint.pprint(json.loads(response.text))
'''

import os
import jwt
import uuid
import hashlib
import pprint
import dotenv
from urllib.parse import urlencode

import requests

dotenv.load_dotenv(dotenv_path=".env")

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

payload = {
  "access_key": access_key,
  "nonce": str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {
  "Authorization": authorize_token
}

res = requests.get(server_url, headers=headers)

pprint.pprint(res.json())