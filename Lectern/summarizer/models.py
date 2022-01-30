from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='media/', null=True)
    transcript = models.CharField(max_length=25000, default='')
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, name, audio_file, poster, is_public=False):
        lecture = cls(name=name, audio_file=audio_file, poster=poster)

        return lecture

