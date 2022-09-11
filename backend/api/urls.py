from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path ("user/create/", views.UserCreateAPIView.as_view ()),
    path ("user/login/", jwt_views.TokenObtainPairView.as_view ()),
    path ("user/token/refresh/", jwt_views.TokenRefreshView.as_view ()),

    path ("songs/", views.SongListCreateAPIView.as_view ()),
    path ("song/<int:pk>/", views.SongDetailAPIView.as_view ()),

    path ("artists/", views.ArtistsAPIView.as_view ()),
    path ("artist/<int:pk>", views.ArtistAPIView.as_view ()),
    path ("artist/<int:pk>/albums/", views.ArtistAlbumsAPIView.as_view ()),
    path ("artist/<int:pk>/songs/", views.ArtistSongsAPIView.as_view ()),

    path ("genres/", views.GenresAPIView.as_view ()),
    path ("genre/<int:pk>/songs/", views.GenreSongsAPIView.as_view ()),
]
