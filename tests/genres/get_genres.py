import requests

endpoint = "https://transfer.lovelacec.org/api/v1/genres/"

request = requests.get (endpoint)
print (request.json ())
