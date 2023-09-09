import requests

host = 'http://localhost:8080/predict'
url ="https://unsplash.com/photos/nDd3dIkkOLo="


data = {"url":  url}
result = requests.post(host, json=data).json()
print(result)
