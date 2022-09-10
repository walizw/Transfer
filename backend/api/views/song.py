from rest_framework import generics

from ..models import Song
from ..models import Album
from ..models import Artist

from ..serializers import SongSerializer

class SongListCreateAPIView (generics.ListCreateAPIView):
    queryset = Song.objects.all ()
    serializer_class = SongSerializer

    def perform_create (self, serializer):
        # Don't do anything yet, TODO: This
        pass
