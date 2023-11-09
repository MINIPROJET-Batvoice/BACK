# Generated by Django 4.2.7 on 2023-11-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0014_alter_transcription_annotator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcription',
            name='annotator_id',
        ),
        migrations.AddField(
            model_name='transcription',
            name='annotator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mini.annotator'),
        ),
    ]
