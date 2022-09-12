from django.urls import path
from . import views

urlpatterns = [
    path ("users/<str:name>", views.UserEndpointView.as_view ()),
    path (".well-known/webfinger", views.WebFingerView.as_view ()),
    path ("users/<str:name>/inbox", views.UserInboxView.as_view ()),
    path ("users/<str:name>/outbox", views.UserOutboxView.as_view ())
]
