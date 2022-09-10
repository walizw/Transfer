import requests

endpoint = "http://localhost:8000/api/v1/user/create/"

data = {
    "name": "user",
    "email": "mail1@example.com",
    "password": "incredible_secure_password123"
}

response = requests.post (endpoint, json=data)
print (response.json ())
