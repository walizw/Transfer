import requests

tok = input ("Enter your access token: ")
sng = input ("Enter your song full path: ")

endpoint = "http://localhost:8000/api/v1/songs/"
data = {
    "audio_file": open (sng, "rb")
}
headers = {
    "Authorization": f"Bearer {tok}"
}

request = requests.post (endpoint, files=data, headers=headers)
print (request.json ())
