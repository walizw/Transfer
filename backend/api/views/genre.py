from rest_framework import generics

from ..models import Genre
from ..models import Song

from ..serializers import GenreSerializer
from ..serializers import SongSerializer

class GenresAPIView (generics.ListAPIView):
    queryset = Genre.objects.all ()
    serializer_class = GenreSerializer

class GenreSongsAPIView (generics.ListAPIView):
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        pk = self.kwargs.get (self.lookup_url_kwarg)
        songs = Song.objects.filter (genre_id=pk)
        return songs
