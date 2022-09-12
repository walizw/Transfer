from rest_framework import generics

from ..models import Song
from ..models import Artist
from ..models import Album

from ..serializers import ArtistSerializer
from ..serializers import SongSerializer
from ..serializers import AlbumSerializer

class ArtistsAPIView (generics.ListAPIView):
    queryset = Artist.objects.all ()
    serializer_class = ArtistSerializer

class ArtistAPIView (generics.RetrieveAPIView):
    queryset = Artist.objects.all ()
    serializer_class = ArtistSerializer

class ArtistSongsAPIView (generics.ListAPIView):
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        pk = self.kwargs.get (self.lookup_url_kwarg)
        songs = Song.objects.filter (artist_id=pk)
        return songs
    
class ArtistAlbumsAPIView (generics.ListAPIView):
    serializer_class = AlbumSerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        pk = self.kwargs.get (self.lookup_url_kwarg)
        albums = Album.objects.filter (artist_id=pk)
        return albums