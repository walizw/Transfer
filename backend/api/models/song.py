from django.db import models

class Song (models.Model):
    # Required fields
    name = models.CharField (max_length=64, default="")

    album_id = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    artist_id = models.DecimalField (max_digits=10, decimal_places=0, default=0)

    audio_file = models.FileField (upload_to="music/")

    # Optional fields
    genre_id = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    lyrics = models.TextField (blank=True, null=True)
    track_number = models.DecimalField (max_digits=4, decimal_places=0, default=0)
    year = models.DecimalField (max_digits=4, decimal_places=0, default=0)
