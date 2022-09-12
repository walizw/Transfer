import requests

username = input ("Enter the name of the user you want to get the endpoint from: ")
endpoint = f"https://transfer.lovelacec.org/users/{username}"

request = requests.get (endpoint)
print (request.json ())
