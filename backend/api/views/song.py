# from rest_framework import generics
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core import files

import io
import uuid

from ..models import Song
from ..models import Album
from ..models import Artist
from ..models import Genre

from ..serializers import SongSerializer
from ..pagers import SmallResultsSetPagination

import music_tag

class SongListCreateAPIView (generics.ListCreateAPIView):
    queryset = Song.objects.all ().order_by ("-pk")
    serializer_class = SongSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create (self, serializer):
        temp_file = serializer.validated_data.get ("audio_file")
        path = temp_file.temporary_file_path ()
        extension = path.split (".")[-1]

        if extension != "mp3" and extension != "wav" and extension != "ogg" and extension != "m4a":
            return Response ("The only supported formats are `mp3', `wav', `ogg' and `m4a'",
                             status=status.HTTP_400_BAD_REQUEST)

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
            matching_album = Album (name=ftag ["album"],
                                    artist_id=artist_id,
                                    year=int (ftag["year"]))
            if ftag ["artwork"].first.data:
                artwork = ftag ["artwork"].first
                thumbnail = artwork.thumbnail ([300, 300])
                format = artwork.mime.split ('/')[1]
                img_name = f"{str (uuid.uuid4 ())}.{format}"

                img_io = io.BytesIO ()
                thumbnail.save (img_io, format)

                img_file = files.File (img_io, name=img_name)
                matching_album.artwork = img_file
            matching_album.save ()

            # Add another album to the artist
            matching_artist.albums += 1
            matching_artist.save ()
        else:
            matching_album = matching_album.get ()

        album_id = matching_album.pk

        # Genre exists?
        matching_genre = Genre.objects.filter (name=ftag ["genre"])
        if not matching_genre.exists ():
            matching_genre = Genre (name=ftag ["genre"])
            matching_genre.save ()
        else:
            matching_genre = matching_genre.get ()

        genre_id = matching_genre.pk

        serializer.save (name=ftag ["title"],
                         album_id=album_id,
                         artist_id=artist_id,
                         genre_id=genre_id,
                         lyrics=ftag ["lyrics"],
                         track_number=int (ftag ["track_number"]),
                         year=int (ftag ["year"]))

        matching_artist.songs += 1
        matching_artist.save ()

        matching_album.songs += 1
        matching_album.save ()

        matching_genre.songs += 1
        matching_genre.save ()

class SongDetailAPIView (generics.RetrieveAPIView):
    queryset = Song.objects.all ()
    serializer_class = SongSerializer
