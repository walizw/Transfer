from rest_framework.renderers import JSONRenderer

class ActivityRenderer (JSONRenderer):
    media_type = "application/activity+json"

class JRDRenderer (JSONRenderer):
    media_type = "application/jrd+json"
