from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from api.models import User

from ..utils.federation import Federation

class FollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"
        activity_id = f"{sender_url}/follows/test"

        follow_request_message = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": activity_id,
            "type": "Follow",
            "actor": sender_url,
            "object": recipient_url
        }

        fedi = Federation (user)
        response = fedi.send_one (recipient_url, follow_request_message)

        return Response (response.status_code)

class UnfollowRemoteAPIView (APIView):
    def post (self, request):
        pass
