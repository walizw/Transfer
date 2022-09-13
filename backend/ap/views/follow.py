from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from api.models import User

from ..models import Activity
from ..utils.federation import Federation
from ..utils.outbox import Outbox

import hashlib

# TODO: Checar que no sigamos dos veces y no dejemos de seguir un usuario que no seguimos
# TODO: Usar el outbox q asquito este codigo

class FollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        outbox = Outbox (user, {
            "type": "Follow",
            "actor": sender_url,
            "object": recipient_url
        }, recipient_url)

        user.following += 1
        user.save ()

        return Response ()

class UnfollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        outbox = Outbox (user, {
            "type": "Unfollow",
            "actor": sender_url,
            "object": recipient_url
        }, recipient_url)

        user.following -= 1
        user.save ()

        return Response ()
