from celery import shared_task


@shared_task
def get_transcript(lecture, filepath):
    return
