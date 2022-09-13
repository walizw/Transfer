from django.db import models

class Activity (models.Model):
    activity_id = models.CharField (max_length=255)
    type = models.CharField (max_length=64)
    actor = models.CharField (max_length=255)
    object = models.TextField ()
