from celery import shared_task
import requests


@shared_task
def get_transcript(lecture, filepath):
    return
