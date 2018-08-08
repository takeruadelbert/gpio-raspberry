import requests

try :
    r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=EUR_USD&compact=y')
    r.raise_for_status()
    print(r.json())
except requests.exceptions.HTTPError as err:
    print(err)
    sys.exit(1)