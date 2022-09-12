import requests

endpoint = f"https://transfer.lovelacec.org/api/v1/songs/"

request = requests.get (endpoint)
print (request.json ())
