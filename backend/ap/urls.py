from django.urls import path
from . import views

urlpatterns = [
    path ("users/<str:name>", views.UserEndpointView.as_view ()),
    path (".well-known/webfinger", views.WebFingerView.as_view ())
]
