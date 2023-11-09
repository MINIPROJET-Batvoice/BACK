import os
from django.contrib.auth.models import User
from django.db import models
from .validator import TextValidator

def audio_directory_path( filename):
    base_path = 'audio'
    return os.path.join(base_path, filename)

class AudioData(models.Model):
    audio_file = models.FileField(upload_to=audio_directory_path)


class CharacterSet(models.Model):
    characters = models.CharField(max_length=200)


class Transcription(models.Model):
    text = models.TextField(validators=[TextValidator])
    audio = models.OneToOneField(AudioData, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)