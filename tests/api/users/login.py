import requests

endpoint = "https://transfer.lovelacec.org/api/v1/user/login/"

name = input ("Enter your username: ")
password = input ("Enter your password: ")

data = {
    "name": name,
    "password": password
}

request = requests.post (endpoint, json=data)
print (request.json ())
