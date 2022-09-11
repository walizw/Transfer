from rest_framework import serializers

from ..models import Song

class SongSerializer (serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "name",
            "album_id",
            "artist_id",
            "audio_file",
            "genre_id",
            "lyrics",
            "track_number",
            "year"
        ]
