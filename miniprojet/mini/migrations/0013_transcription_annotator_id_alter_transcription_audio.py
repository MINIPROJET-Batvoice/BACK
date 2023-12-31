# Generated by Django 4.2.7 on 2023-11-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0012_alter_audiodata_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcription',
            name='annotator_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mini.annotator'),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='audio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mini.audiodata'),
        ),
    ]
