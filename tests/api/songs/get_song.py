import requests

song_id = input ("Enter the ID of the song you want to get: ")
endpoint = f"http://localhost:8000/api/v1/song/{song_id}/"

request = requests.get (endpoint)
print (request.json ())
