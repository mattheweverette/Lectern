from django import forms
from .models import Lecture
from django.core.exceptions import ValidationError


class AudioFileForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ["name", "audio_file"]

    def clean(self):
        cleaned_data = super().clean()
        filename = cleaned_data.get("audio_file").name

        if filename[-4:] != '.mp3':
            raise ValidationError(f"Wrong file type: '{filename}'. Please upload an mp3")

