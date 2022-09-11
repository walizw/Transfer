import requests

artist_id = input ("Enter the Artist ID to get the albums from: ")
endpoint = f"http://localhost:8000/api/v1/artist/{artist_id}/albums/"

request = requests.get (endpoint)
print (request.json ())
