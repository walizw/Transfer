from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User

from django.conf import settings

class UserEndpointView (APIView):
    media_type = "application/activity+json"

    def get (self, request, name):
        user = User.objects.filter (name=name)
        if len (user) == 0:
            return Response ("Error: The entered user does not exist!")

        user = user.get ()
        user_url = f"{settings.DOMAIN_NAME}/api/v1/users/{name}"
        response = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
            ],
            "id": f"{user_url}",
            "inbox": f"{user_url}/inbox",
            "outbox": f"{user_url}/outbox",
            "type": "Person",
            "name": name,
            "preferredUsername": name,
            "publicKey": {
                "id": f"{user_url}#main-key",
                "owner": user_url,
                "publicKeyPem": user.pub_key
            }
        }

        res = Response (response)
        res.content_type = "application/activity+json"
        return res

class WebFingerView (APIView):
    media_type = "application/jrd+json"

    def get (self, request):
        resource = request.GET ["resource"]
        user = resource.split (":")[1].split ("@")[0]
        user_url = f"{settings.DOMAIN_NAME}/api/v1/users/{user}"
        response = {
            "subject": resource,
            "links": [
                {
                    "rel": "self",
                    "type": "application/activity+json",
                    "href": f"{user_url}"
                }
            ]
        }

        res = Response (response)
        res.content_type = "application/jrd+json"
        return res

class UserInboxView (APIView):
    media_type = "application/activity+json"

    def post (self, request, *args, **kwargs):
        return Response ("TODO")

class UserOutboxView (APIView):
    media_type = "application/activity+json"

    def post (self, request, *args, **kwargs):
        return Response ("TODO")
