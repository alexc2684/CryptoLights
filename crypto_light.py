#!/usr/bin/python
import requests
import json
import os 

LIGHT1_IP = os.environ['LIGHT1_IP']
PHILIPS_USER = os.environ['PHILIPS_USER']
CRYPTO_COMPARE_KEY = os.environ['CRYPTO_COMPARE_KEY']

data = requests.get("https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&e=Kraken&api_key=" + CRYPTO_COMPARE_KEY + "").content

data = json.loads(data)

delta = data["RAW"]["CHANGEPCT24HOUR"]

if delta > 0:
	hue = 14000 + delta*1000
else:
	hue = 58000 + (-delta)*1000

payload = '{"on": true, "sat":100, "bri":50,"hue": ' + str(int(hue)) + '}'
print(payload)

res = requests.put("http://" + LIGHT1_IP + "/api/" + PHILIPS_USER + "/lights/1/state", data=payload)

print(res)
