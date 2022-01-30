from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='media/', null=True)
    summary = models.JSONField(default=dict)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)

    @classmethod
    def create(cls, name, audio_file, poster, is_public=False):
        lecture = cls(name=name, audio_file=audio_file, poster=poster)

        return lecture

    
    def get_absolute_url(self):
        return reverse('lecture', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.poster.username + "-" + self.name)
        return super().save(*args, **kwargs)

