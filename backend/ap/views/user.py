from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User

from django.conf import settings

class UserEndpointView (APIView):
    def get (self, request, name):
        user = User.objects.filter (name=name)
        if len (user) == 0:
            return Response ("Error: The entered user does not exist!")

        user = user.get ()
        user_url = f"{settings.DOMAIN_NAME}/users/{name}"
        response = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": f"{user_url}",
            "inbox": f"{user_url}/inbox",
            "outbox": f"{user_url}/outbox",
            "type": "Person",
            "name": name
        }

        res = Response (response)
        res.content_type = "application/activity+json"
        return res
