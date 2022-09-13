from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from api.models import User

from cryptography.hazmat.backends import default_backend as crypto_default_backend
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from urllib.parse import urlparse
import base64
import datetime
import requests

class FollowRemoteAPIView (APIView):
    def post (self, request):
        username = request.user
        user = User.objects.filter (name=username).get ()

        recipient_url = request.POST ["recipient"]
        recipient_inbox = f"{recipient_url}/inbox"

        sender_url = f"{settings.DOMAIN_NAME}/api/v1/users/{username}"
        sender_key = f"{sender_url}#main-key"

        activity_id = f"{sender_url}/follows/test"

        private_key_text = user.priv_key.encode ()
        private_key = crypto_serialization.load_pem_private_key (
            private_key_text,
            password = None
        )

        current_date = datetime.datetime.utcnow ().strftime ("%a, %d %b %Y %H:%M:%S GMT")

        recipient_parsed = urlparse (recipient_inbox)
        recipient_host = recipient_parsed.netloc
        recipient_path = recipient_parsed.path

        signature_text = b"(request-target): post %s\nhost: %s\ndate: %s" % (recipient_path.encode ("utf-8"), recipient_host.encode ("utf-8"), current_date.encode ("utf-8"))

        raw_signature = private_key.sign (
            signature_text,
            padding.PKCS1v15 (),
            hashes.SHA256 ()
        )

        signature_header = 'keyId="%s",algorithm="rsa-sha256",headers="(request-target) host date",signature="%s"' % (sender_key, base64.b64encode (raw_signature).decode ('utf-8'))

        headers = {
            "Date": current_date,
            "Content-Type": "application/activity+json",
            "Host": recipient_host,
            "Signature": signature_header
        }

        follow_request_message = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": activity_id,
            "type": "Follow",
            "actor": sender_url,
            "object": recipient_url
        }

        request = requests.post (recipient_inbox, headers=headers, json=follow_request_message)
        return Response (request.content)
