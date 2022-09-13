from django.urls import path
from . import views

urlpatterns = [
    path ("users/<str:name>", views.UserEndpointView.as_view ()),
    path ("users/<str:name>/inbox", views.UserInboxView.as_view ()),
    path ("users/<str:name>/outbox", views.UserOutboxView.as_view ()),

    path ("user/remote_follow/", views.FollowRemoteAPIView.as_view ()),
    path ("user/remote_unfollow/", views.UnfollowRemoteAPIView.as_view ())
]
