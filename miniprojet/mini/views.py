import os
from pathlib import Path
import json
from random import choice
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.http import FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import AudioData, CharacterSet
from .models import Transcription
from .validator import TextValidator

@require_http_methods(["GET"])
def list_audios(request):
    all_audios = list(AudioData.objects.values())
    return JsonResponse(all_audios, safe=False)

@require_http_methods(["GET"])
def get_audio(request, audio_id):
    audio = AudioData.objects.get(pk=audio_id)
    audio_path = Path('F:/Desktop/batvoice/audio', audio.audio_file.name)
    with audio_path.open('rb') as file:
        response = FileResponse(file, content_type='audio/mpeg')
    return response


def populate_data(directory_path):
    audio_data_list = populate_audio_data_from_directory(directory_path)
    print("Data population complete:", audio_data_list)

def populate_audio_data_from_directory(directory_path):
    audio_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    audio_data_list = []
    for audio_file in audio_files:
        if audio_file.endswith('.mp3'):
            audio_file_path = os.path.join('audio', audio_file)
            if not AudioData.objects.filter(audio_file=audio_file_path).exists():
                audio_data = AudioData.objects.create(audio_file=audio_file_path)
                audio_data_list.append({'id': audio_data.id, 'audio_file': audio_data.audio_file.name})
                audio_data.save()
                print(f"Added audio data for {audio_file_path}")
            else:
                print(f"Audio data for {audio_file_path} already exists")
    return audio_data_list


directory_path = 'F:/Desktop/batvoice/audio'
populate_data(directory_path)



@require_http_methods(["GET"])
def untranscribed_audios(request):
    untranscribed_audios = []

    all_audios = AudioData.objects.all()
    for audio in all_audios:
        if not Transcription.objects.filter(audio=audio).exists():
            untranscribed_audios.append(audio.audio_file.name)

    return JsonResponse(untranscribed_audios, safe=False)


@require_http_methods(["GET"])
def get_random_untranscribed_audio(request):
    untranscribed_audios = []

    all_audios = AudioData.objects.filter(transcription__isnull=True)
    if all_audios:
        random_audio = choice(all_audios)
        untranscribed_audios.append({
            'audio_name': random_audio.audio_file.name,
            'audio_id': random_audio.id,
        })
        print("Response object ID:", random_audio.id)

    return JsonResponse(untranscribed_audios, safe=False)

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'})

        user = User.objects.create_user(username, email, password)
        user.save()
        print('User registered successfully')
        return JsonResponse({'success': 'User registered successfully'})
    else:
        print('Invalid request method')
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response_data = {'user': user.id, 'message': 'Login successful', 'csrf_token': get_token(request)}
            print(response_data)
            return JsonResponse(response_data)
        else:
            response_data = {'message': 'Invalid credentials'}
            print(response_data)
            return JsonResponse(response_data, status=401)

    response_data = {'message': 'Only POST requests are allowed', 'csrf_token': get_token(request)}
    print(response_data)
    return JsonResponse(response_data, status=400)

def create_character_set(characters):
    character_set, created = CharacterSet.objects.get_or_create(characters=characters)
    if created:
        print("Character set created successfully:", characters)
    else:
        print("Character set already exists:", characters)

characters = "()'aAàÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
create_character_set(characters)

@csrf_exempt
@require_http_methods(["POST"])
def add_transcription(request, user_id, audio_id):
    data = json.loads(request.body)
    transcription_text = data.get('transcription_text')

    character_set = CharacterSet.objects.first().characters

    validator = TextValidator(character_set=set(character_set))
    error_messages = []

    if not validator.validate(transcription_text, error_messages):
        print("Detected errors:", error_messages)  # Display error messages in the Django console
        return JsonResponse({'success': False, 'errors': error_messages}, status=400)

    user = get_object_or_404(User, pk=user_id)
    audio = get_object_or_404(AudioData, pk=audio_id)

    try:
        new_transcription = Transcription.objects.create(text=transcription_text, audio=audio, user=user)
        return JsonResponse({'success': True, 'message': 'Transcription added successfully'})
    except Exception as e:
        print("An error occurred while creating  transcription:", str(e))
        return JsonResponse({'success': False, 'message': str(e)})
