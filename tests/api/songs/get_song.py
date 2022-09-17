import requests

song_id = input ("Enter the ID of the song you want to get: ")
endpoint = f"https://transfer.lovelacec.org/api/v1/song/{song_id}/"

request = requests.get (endpoint)
print (request.json ())
