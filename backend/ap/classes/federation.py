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
import json
import hashlib

class Federation ():
    recipient = ""
    recipient_inbox = ""
    recipient_host = ""

    actor = None
    actor_key = ""

    digest = ""

    private_key = ""
    raw_signature = ""

    def __init__ (self, actor):
        self.actor = actor
        self.serialize_private_key ()

    def send_one (self, recipient, message):
        self.recipient = recipient

        self.recipient_inbox = f"{self.recipient}/inbox"
        recipient_parsed = urlparse (self.recipient_inbox)
        self.recipient_host = recipient_parsed.netloc
        actor_url = f"{settings.DOMAIN_NAME}/api/v1/users/{self.actor.name}"
        self.actor_key = f"{actor_url}#main-key"

        current_date = datetime.datetime.utcnow ().strftime ("%a, %d %b %Y %H:%M:%S GMT")

        digest = self.gen_digest (message)
        signature = self.gen_signature (digest, current_date)
        signature_header = self.gen_signature_header (signature)

        headers = {
            "Date": current_date,
            "Content-Type": "application/activity+json",
            "Host": self.recipient_host,
            "Digest": f"SHA-256={digest.decode ('utf-8')}",
            "Signature": signature_header
        }

        request = requests.post (self.recipient_inbox, headers=headers, json=message)
        return request

    def gen_signature (self, digest, date):
        recipient_parsed = urlparse (self.recipient_inbox)
        recipient_path = recipient_parsed.path

        signature_text = b"(request-target): post %s\ndigest: SHA-256=%s\nhost: %s\ndate: %s" % (recipient_path.encode ("utf-8"), digest, self.recipient_host.encode ("utf-8"), date.encode ("utf-8"))

        raw_signature = self.private_key.sign (
            signature_text,
            padding.PKCS1v15 (),
            hashes.SHA256 ()
        )
        return raw_signature

    def gen_signature_header (self, raw_signature):
        return 'keyId="%s",algorithm="rsa-sha256",headers="(request-target) digest host date",signature="%s"' % (self.actor_key, base64.b64encode (raw_signature).decode ("utf-8"))

    def gen_digest (self, data):
        json_string = json.dumps (data)
        digest = base64.b64encode (hashlib.sha256 (json_string.__str__ ().encode ("utf-8")).digest ())
        return digest

    def serialize_private_key (self):
        private_key_text = self.actor.priv_key.encode ()
        self.private_key = crypto_serialization.load_pem_private_key (
            private_key_text,
            password = None,
            backend = crypto_default_backend ()
        )
