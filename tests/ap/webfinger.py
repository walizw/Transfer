import requests

name = input ("Enter the name of the user you want to get the webfinger of: ")
endpoint = "https://transfer.lovelacec.org/.well-known/webfinger"

request = requests.get (endpoint, params={
    "resource": f"acct:{name}@transfer.lovelacec.org"
})
print (request.json ())
