import requests

genre_id = input ("Enter the ID of the genre you want to get the songs from: ")
endpoint = f"http://localhost:8000/api/v1/genre/{genre_id}/songs/"

request = requests.get (endpoint)
print (request.json ())
