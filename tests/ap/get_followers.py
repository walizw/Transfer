import requests

user = input ("Enter the user you want to get the `followers' of: ")
endpoint = f"https://transfer.lovelacec.org/api/v1/users/{user}/followers?page=1"

request = requsts.get (endpoint)
print (request.json ())
