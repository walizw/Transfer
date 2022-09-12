import requests

endpoint = "https://transfer.lovelacec.org/api/v1/artists/"
request = requests.get (endpoint)
print (request.json ())
