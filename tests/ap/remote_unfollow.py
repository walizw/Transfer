import requests

tok = input ("Enter your access token: ")
rmt = input ("Enter the url of the remote user to unfollow: ")

endpoint = "https://transfer.lovelacec.org/api/v1/user/remote_unfollow/"
headers = {
    "Authorization": f"Bearer {tok}"
}
data = {
    "recipient": rmt
}

request = requests.post (endpoint, data=data, headers=headers)
print (request.json ())
