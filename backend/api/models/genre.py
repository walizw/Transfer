from django.db import models

class Genre (models.Model):
    # Required fields
    name = models.CharField (max_length=64)

    # Optional fields
    about = models.TextField (blank=True, null=True)
    artwork = models.ImageField (upload_to="artworks/genres/", blank=True, null=True)
    songs = models.DecimalField (max_digits=4, decimal_places=0, default=0)
