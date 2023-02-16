import requests

f = open("apikey", "r")
key = f.read()
f.close()
del(f)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=' + str(key)
r = requests.get(url)
data = r.json()

print(data)
