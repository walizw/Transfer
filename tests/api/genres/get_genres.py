import requests

endpoint = "http://localhost:8000/api/v1/genres/"

request = requests.get (endpoint)
print (request.json ())
