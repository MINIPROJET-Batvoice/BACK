from rest_framework import serializers
from .models import AudioData

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioData
        fields = '__all__'
