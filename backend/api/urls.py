from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path ("user/create/", views.UserCreateAPIView.as_view ()),
    path ("user/login/", jwt_views.TokenObtainPairView.as_view ()),
    path ("user/token/refresh/", jwt_views.TokenRefreshView.as_view ()),

    path ("songs/", views.SongListCreateAPIView.as_view ()),
]
