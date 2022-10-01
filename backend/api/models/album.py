from django.db import models

class Album (models.Model):
    # Required fields
    name = models.CharField (max_length=64)
    artist_id = models.DecimalField (max_digits=10, decimal_places=0) # The artist id this album belongs to

    # Optional fields
    artwork = models.FileField (upload_to="artworks/", blank=True, null=True)
    songs = models.DecimalField (max_digits=4, decimal_places=0, default=0)
    year = models.DecimalField (max_digits=5, decimal_places=0, default=0)
