import requests

endpoint = "https://transfer.lovelacec.org/api/v1/albums/"

request = requests.get (endpoint)
print (request.json ())
