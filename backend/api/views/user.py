from rest_framework import generics
from django.contrib.auth.hashers import make_password

from ..models import User
from ..utils.keys_gen import gen_keypair
from ..serializers import PrivateUserSerializer

class UserCreateAPIView (generics.CreateAPIView):
    queryset = User.objects.all ()
    serializer_class = PrivateUserSerializer

    def perform_create (self, serializer):
        password = serializer.validated_data.get ("password")
        total_users = len (User.objects.all ())
        
        is_admin = True if total_users == 0 else False
        hashed_password = make_password (password, None, "pbkdf2_sha256")
        pair = gen_keypair ()
        serializer.save (password=hashed_password, is_admin=is_admin,
                         is_superuser=is_admin,
                         is_staff=is_admin,
                         priv_key=pair ["priv_key"],
                         pub_key=pair ["pub_key"])
