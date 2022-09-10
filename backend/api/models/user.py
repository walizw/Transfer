from django.db import models
from django.utils import timezone

class User (models.Model):
    # Required fields
    name = models.CharField (max_length=32, unique=True)
    email = models.EmailField ()
    password = models.CharField (max_length=125)

    # With default values fields
    bio = models.TextField (blank=True, null=True)
    
    creation_date = models.DateTimeField (default=timezone.now)
    is_admin = models.BooleanField (default=False)
    followers = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    following = models.DecimalField (max_digits=10, decimal_places=0, default=0)
