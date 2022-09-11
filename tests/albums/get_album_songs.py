import requests

album_id = input ("Enter the album ID to get the songs from: ")
endpoint = f"http://localhost:8000/api/v1/album/{album_id}/songs/"

request = requests.get (endpoint)
print (request.json ())
