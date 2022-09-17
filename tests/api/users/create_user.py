import requests

endpoint = "https://transfer.lovelacec.org/api/v1/user/create/"

username = input ("Enter the name for the newly created user: ")
password = input ("Enter the password for the newly created user: ")

data = {
    "name": username,
    "email": "demo@example.com",
    "password": password
}

request = requests.post (endpoint, json=data)
print (request.json ())
