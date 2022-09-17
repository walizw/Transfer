from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from api.models import User

from ..models import Activity
from ..classes.federation import Federation

import requests

# TODO: Checar que no sigamos dos veces y no dejemos de seguir un usuario que no seguimos

class FollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        requests.post (f"{sender_url}/outbox", {
            "type": "Follow",
            "actor": sender_url,
            "object": recipient_url
        })

        user.following += 1
        user.save ()

        return Response ()

class UnfollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        requests.post (f"{sender_url}/outbox", {
            "type": "Unfollow",
            "actor": sender_url,
            "object": recipient_url
        })

        user.following -= 1
        user.save ()

        return Response ()
