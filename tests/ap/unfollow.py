import requests

tok = input ("Enter your access token: ")
rmt = input ("Enter the url of the user to unfollow: ")

endpoint = "http://localhost:8000/api/v1/user/unfollow/"
headers = {
    "Authorization": f"Bearer {tok}"
}
data = {
    "recipient": rmt
}

request = requests.post (endpoint, data=data, headers=headers)
print (request.content.decode ())
