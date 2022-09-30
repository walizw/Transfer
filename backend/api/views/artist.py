from rest_framework import generics, permissions

from ..models import Song
from ..models import Artist
from ..models import Album

from ..pagers import SmallResultsSetPagination

from ..serializers import ArtistSerializer
from ..serializers import SongSerializer
from ..serializers import AlbumSerializer

class ArtistsAPIView (generics.ListAPIView):
    queryset = Artist.objects.all ().order_by ("-pk")
    serializer_class = ArtistSerializer
    pagination_class = SmallResultsSetPagination

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
        albums = Album.objects.filter (artist_id=pk).order_by ("-year")
        return albums

class ArtistUpdateAPIView (generics.UpdateAPIView):
    queryset = Artist.objects.all ()
    serializer_class = ArtistSerializer
    lookup_url_kwarg = "pk"
    permission_classes = [permissions.IsAuthenticated]
