# Generated by Django 4.2.7 on 2023-11-06 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0018_remove_transcription_annotator_transcription_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Annotator',
        ),
    ]