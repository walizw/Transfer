import requests

artist_id = input ("Enter the id of the artist: ")
endpoint = f"https://transfer.lovelacec.org/api/v1/artist/{artist_id}"

request = requests.get (endpoint)
print (request.json ())
