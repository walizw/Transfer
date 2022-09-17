import requests

album_id = input ("Enter the album ID to get the songs from: ")
endpoint = f"https://transfer.lovelacec.org/api/v1/album/{album_id}/songs/"

request = requests.get (endpoint)
print (request.json ())
