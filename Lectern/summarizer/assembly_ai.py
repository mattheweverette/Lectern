from .models import Lecture
from celery import shared_task
import time


def handle_uploaded_file(user, name, file, poster):
    with open(f'media/{file.name}', "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    lecture = Lecture.create(name, file.name, poster)
    lecture.save()

    get_transcript.delay(f'media/{file.name}')


@shared_task
def get_transcript(filepath):
    return
