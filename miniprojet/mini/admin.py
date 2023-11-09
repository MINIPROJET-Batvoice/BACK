from django.contrib import admin
from .models import AudioData, Transcription

admin.site.register(AudioData)
admin.site.register(Transcription)
