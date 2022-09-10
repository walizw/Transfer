from rest_framework import generics

from ..models import Song
from ..models import Artist
from ..models import Album

from ..serializers import ArtistSerializer

class ArtistsAPIView (generics.ListAPIView):
    queryset = Artist.objects.all ()
    serializer_class = ArtistSerializer

class ArtistAPIView (generics.RetrieveAPIView):
    queryset = Artist.objects.all ()
    serializer_class = ArtistSerializer

class ArtistSongsAPIView (generics.ListAPIView):
    # TODO: This
    pass
    
class ArtistAlbumsAPIView (generics.ListAPIView):
    # TODO: This
    pass
