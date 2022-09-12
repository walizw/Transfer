from rest_framework import serializers

from ..models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "bio",
            "creation_date",
            "followers",
            "following"
        ]

class PrivateUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "pub_key",
            "priv_key",
            "is_admin"
        ]
