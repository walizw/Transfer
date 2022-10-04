from rest_framework import serializers

from ..models import Song, Album, Artist

class SongSerializer (serializers.ModelSerializer):
    album = serializers.SerializerMethodField ()
    artist = serializers.SerializerMethodField ()

    def get_album (self, instance):
        album = Album.objects.all ().filter (id=instance.album_id).get ()
        return {
            "id": album.id,
            "name": album.name,
            "artwork": album.artwork.url,
            "songs": album.songs,
            "year": album.year
        }

    def get_artist (self, instance):
        artist = Artist.objects.all ().filter (id=instance.artist_id).get ()
        return {
            "id": artist.id,
            "name": artist.name,
            "pfp": artist.pfp.url if artist.pfp else None
        }

    class Meta:
        model = Song
        fields = [
            "id",
            "name",
            "album",
            "artist",
            "audio_file",
            "genre_id",
            "lyrics",
            "track_number",
            "year"
        ]
