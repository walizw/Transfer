from django.db import models

class Artist (models.Model):
    # Required fields
    name = models.CharField (max_length=64)

    # Optional fields
    pfp = models.ImageField (upload_to="artist_pfps/", blank=True, null=True)
    bio = models.TextField (blank=True, null=True)
    songs = models.DecimalField (max_digits=10, decimal_places=0, default=0) # No of songs
    albums = models.DecimalField (max_digits=10, decimal_places=0, default=0) # No of albums
    followers = models.DecimalField (max_digits=10, decimal_places=0, default=0)
