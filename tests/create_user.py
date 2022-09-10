import requests

endpoint = "http://localhost:8000/api/v1/user/create/"

data = {
    "name": "demo_user",
    "email": "demo@example.com",
    "password": "demo_password"
}

request = requests.post (endpoint, json=data)
print (request.json ())
