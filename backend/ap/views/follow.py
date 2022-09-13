from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from api.models import User

from ..models import Activity
from ..utils.federation import Federation

import hashlib

class FollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        activity_hash = hashlib.new ("md5", str (len (Activity.objects.all ())).encode ()).digest ()
        activity_id = f"{sender_url}/follows/{activity_hash}"

        follow_request_message = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": activity_id,
            "type": "Follow",
            "actor": sender_url,
            "object": recipient_url
        }

        fedi = Federation (user)
        response = fedi.send_one (recipient_url, follow_request_message)

        act = Activity (activity_id=activity_id, type="Follow", actor=sender_url, object=recipient_url)
        act.save ()

        user.following += 1
        user.save ()

        return Response (response.content.decode ())

class UnfollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"

        activity_hash = hashlib.new ("md5", str (len (Activity.objects.all ())).encode ()).digest ()
        activity_id = f"{sender_url}/follows/{activity_hash}/undo"

        follow_activity = Activity.objects.filter (actor=sender_url, object=recipient_url)
        if len (follow_activity) < 1:
            print (f"The activity where {sender_url} follows {recipient_url} doesn't exist")
            return Response ("Error")
        follow_activity = follow_activity.get ()

        follow_request_message = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": activity_id,
            "type": "Undo",
            "actor": sender_url,
            "object": {
                "id": follow_activity.activity_id,
                "type": "Follow",
                "actor": sender_url,
                "object": recipient_url
            }
        }

        fedi = Federation (user)
        response = fedi.send_one (recipient_url, follow_request_message)
        follow_activity.delete ()

        user.following -= 1
        user.save ()

        return Response (response.content.decode ())
