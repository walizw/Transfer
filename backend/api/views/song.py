# from rest_framework import generics
from rest_framework import generics, permissions

from ..models import Song
from ..models import Album
from ..models import Artist

from ..serializers import SongSerializer

import music_tag

class SongListCreateAPIView (generics.ListCreateAPIView):
    queryset = Song.objects.all ()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create (self, serializer):
        temp_file = serializer.validated_data.get ("audio_file")
        path = temp_file.temporary_file_path ()

        ftag = music_tag.load_file (path)

        # Artist exists?
        matching_artist = Artist.objects.filter (name=ftag ["artist"])
        if not matching_artist.exists ():
            matching_artist = Artist (name=ftag ["artist"])
            matching_artist.save ()
        else:
            matching_artist = matching_artist.get ()

        artist_id = matching_artist.pk

        # Album exists?
        matching_album = Album.objects.filter (name=ftag ["album"], artist_id=artist_id)
        if not matching_album.exists ():
            matching_album = Album (name=ftag ["album"], artist_id=artist_id)
            matching_album.save ()

            # Add another album to the artist
            matching_artist.albums += 1
            matching_artist.save ()
        else:
            matching_album = matching_album.get ()

        album_id = matching_album.pk

        serializer.save (name=ftag ["title"],
                         album_id=album_id,
                         artist_id=artist_id,
                         genre=ftag ["genre"],
                         lyrics=ftag ["lyrics"],
                         track_number=int (ftag ["track_number"]),
                         year=int (ftag ["year"]))

        matching_artist.songs += 1
        matching_artist.save ()

        matching_album.songs += 1
        matching_album.save ()

class SongDetailAPIView (generics.RetrieveAPIView):
    queryset = Song.objects.all ()
    serializer_class = SongSerializer
