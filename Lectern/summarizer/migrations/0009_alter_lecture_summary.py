# Generated by Django 4.0.1 on 2022-01-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0008_remove_lecture_transcript_lecture_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='summary',
            field=models.JSONField(default=dict),
        ),
    ]