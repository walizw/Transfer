from django.urls import path

from . import views

urlpatterns = [
    path ("user/create/", views.UserCreateAPIView.as_view ()),
]
