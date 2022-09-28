import requests

name = input ("Enter the name of the user you want to get the webfinger of: ")
endpoint = "http://localhost:8000/.well-known/webfinger"

request = requests.get (endpoint, params={
    "resource": f"acct:{name}@transfer.lovelacec.org"
})
print (request.json ())
