# Generated by Django 4.0.1 on 2022-01-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_file', models.CharField(max_length=50)),
                ('lecture_transcript', models.CharField(max_length=25000)),
                ('is_lecture_public', models.BooleanField(default=False)),
            ],
        ),
    ]
