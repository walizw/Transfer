from rest_framework import serializers

from ..models import Artist

class ArtistSerializer (serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "pk",
            "name",
            "pfp",
            "bio",
            "songs",
            "albums",
            "followers"
        ]
