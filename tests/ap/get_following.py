import requests

user = input ("Enter the user you want to get the `following': ")
endpoint = f"https://transfer.lovelacec.org/api/v1/users/{user}/following?page=1"

request = requests.get (endpoint)
print (request.json ())
