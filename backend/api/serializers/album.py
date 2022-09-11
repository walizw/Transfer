from rest_framework import serializers

from ..models import Album

class AlbumSerializer (serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "artist_id",
            "artwork",
            "songs"
        ]
