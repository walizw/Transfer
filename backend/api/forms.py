from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class _UserCreationForm (UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password")

class _UserChangeForm (UserChangeForm):
    class Meta:
        model = User
        fields = ("name", "email", "password")
