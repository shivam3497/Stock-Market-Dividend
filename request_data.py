import requests
import json
#print(help(requests))
def stockData():
    r = requests.get('https://api.polygon.io/v2/reference/dividends/AAPL?apiKey=decD_6xWhZQIer0Vd_wdvD_2GEFLmYZ8')
    #print(r)
    #print(help(r))
    #print(r.json().dump(indent=4))
    return json.dumps(r.json(),indent=4)
    #print(help(json))
