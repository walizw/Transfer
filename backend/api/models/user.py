from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager (BaseUserManager):
    def create_user (self, name, email, password, **extra_fields):
        if not name:
            raise ValueError ("The name must be set")

        if not email:
            raise ValueError ("The mail must be set")

        email = self.normalize_email (email)
        user = self.model (name=name, email=email, **extra_fields)
        user.set_password (password)
        user.save ()
        return user

    def create_superuser (self, name, email, password, **extra_fields):
        extra_fields.setdefault ("is_staff", True)
        extra_fields.setdefault ("is_superuser", True)
        extra_fields.setdefault ("is_admin", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser must have is_admin=True.")

        return self.create_user(name, email, password, **extra_fields)

class User (AbstractBaseUser, PermissionsMixin):
    # Required fields
    name = models.CharField (max_length=32, unique=True)
    email = models.EmailField (unique=True)
    password = models.CharField (max_length=125)

    # With default values fields
    bio = models.TextField (blank=True, null=True)
    
    creation_date = models.DateTimeField (default=timezone.now)
    followers = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    following = models.DecimalField (max_digits=10, decimal_places=0, default=0)

    is_staff = models.BooleanField (default=False)
    is_superuser = models.BooleanField (default=False)
    is_admin = models.BooleanField (default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ["email", "password"]

    objects = UserManager ()

    def __str__ (self):
        return self.name
