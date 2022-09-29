from rest_framework import generics

from ..models import Album
from ..models import Song

from ..serializers import AlbumSerializer
from ..serializers import SongSerializer

class AlbumsAPIView (generics.ListAPIView):
    queryset = Album.objects.all ()
    serializer_class = AlbumSerializer

class AlbumAPIView (generics.RetrieveAPIView):
    queryset = Album.objects.all ()
    serializer_class = AlbumSerializer

class AlbumSongsAPIView (generics.ListAPIView):
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        pk = self.kwargs.get (self.lookup_url_kwarg)
        songs = Song.objects.filter (album_id=pk)
        return songs
