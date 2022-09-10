import requests

endpoint = "http://localhost:8000/api/v1/artists/"
request = requests.get (endpoint)
print (request.json ())
