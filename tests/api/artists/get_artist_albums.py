import requests

artist_id = input ("Enter the Artist ID to get the albums from: ")
endpoint = f"https://transfer.lovelacec.org/api/v1/artist/{artist_id}/albums/"

request = requests.get (endpoint)
print (request.json ())
