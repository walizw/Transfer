import requests

artist_id = input ("Enter the id of the artist: ")
endpoint = f"http://localhost:8000/api/v1/artist/{artist_id}"

request = requests.get (endpoint)
print (request.json ())
