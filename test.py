import requests

url = 'http://localhost:9696/predict'

data = {'path':  './images/0004.jpg'}

result = requests.post(url, json=data).json()
print(result)