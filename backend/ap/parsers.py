from rest_framework.parsers import BaseParser

class ActivityParser (BaseParser):
    media_type = "application/activity+json"

    def parse (self, stream, media_type=None, parser_context=None):
        return stream.read ()
