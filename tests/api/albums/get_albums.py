import requests

endpoint = "http://localhost:8000/api/v1/albums/"

request = requests.get (endpoint)
print (request.json ())
