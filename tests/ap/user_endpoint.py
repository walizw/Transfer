import requests

username = input ("Enter the name of the user you want to get the endpoint from: ")
endpoint = f"http://localhost:8000/users/{username}"

request = requests.get (endpoint)
print (request.json ())
