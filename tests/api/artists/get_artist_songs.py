import requests

artist_id = input ("Enter the artist ID to get the songs from: ")
endpoint = f"http://localhost:8000/api/v1/artist/{artist_id}/songs/"

request = requests.get (endpoint)
print (request.json ())
