import sys
import requests
import json

req_calc = float(sys.argv[1])

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rj = r.json()
    usd_rate = rj.get("bpi", {}).get("USD", {}).get("rate")
except requests.RequestException:
    print("Request error")
usd_rate_float = float((usd_rate).replace(",", "").replace("'", ""))

rounded = round(req_calc*usd_rate_float, 4)
print("$" + "{:,}".format(rounded), end="")
