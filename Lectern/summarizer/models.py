from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='media/', null=True)
    transcript = models.CharField(max_length=25000, default='')
    is_public = models.BooleanField(default=False)

