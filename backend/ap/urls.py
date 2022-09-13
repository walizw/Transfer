from django.urls import path
from . import views

urlpatterns = [
    path ("users/<str:name>", views.UserEndpointView.as_view ()),
    path ("users/<str:name>/inbox", views.UserInboxView.as_view ()),
    path ("users/<str:name>/outbox", views.UserOutboxView.as_view ()),
    path ("users/<str:name>/following", views.UserFollowingView.as_view ()),
    path ("users/<str:name>/followers", views.UserFollowersView.as_view ()),

    path ("user/follow/", views.FollowRemoteAPIView.as_view ()),
    path ("user/unfollow/", views.UnfollowRemoteAPIView.as_view ())
]
