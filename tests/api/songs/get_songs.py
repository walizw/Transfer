import requests

endpoint = f"http://localhost:8000/api/v1/songs/"

request = requests.get (endpoint)
print (request.json ())
