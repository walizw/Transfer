from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import User
from ..models import Activity

from django.conf import settings

import json
import urllib.parse

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
            "followers": f"{user_url}/followers",
            "following": f"{user_url}/following",
            "liked": f"{user_url}/liked",
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

    def post (self, request, name):
        data = json.loads (request.data.decode ("utf-8"))
        
        act_id = data ["id"]
        act_type = data ["type"]
        act_actor = data ["actor"]
        act_object = data ["object"]

        if act_type == "Follow":
            user = User.objects.filter (name=name)
            if len (user) < 1:
                print (f"{act_actor} tried to follow a user that does not exist")
                return Response ("The entered user does not exist")
            user = user.get ()
            user.followers += 1
            user.save ()

            activity = Activity (activity_id=act_id, type=act_type, actor=act_actor, object=act_object)
            activity.save ()

            print (f"{act_actor} followed {act_object}.")
            return Response ("Success")
        elif act_type == "Create":
            # TODO: Process create
            pass
        elif act_type == "Undo":
            user = User.objects.filter (name=name)
            if len (user) < 1:
                print (f"{act_actor} tried to undo an activity to a user that does not exist")
                return Response ("The entered user does not exist")
            user = user.get ()

            if act_object ["type"] == "Follow":
                # Unfollow
                activity = Activity.objects.filter (activity_id=act_object ["id"])
                if len (activity) < 1:
                    print (f"The activity {act_object ['id']} does not exist")
                    return Response ("The activity does not exist")
                activity.delete () # TODO: Necesitamos dejarla en la base de datos?
                # TODO: Necesitamos almacenar este Undo en la base de datos?

                print (f"{act_actor} unfollowed {act_object ['object']}")
                user.followers -= 1
                user.save ()
                return Response ("Success")

        return Response ("There's been an error processing your request.")

class UserOutboxView (APIView):
    media_type = "application/activity+json"

    def post (self, request, name):
        return Response ("TODO")
