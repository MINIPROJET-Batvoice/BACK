# Generated by Django 4.2.7 on 2023-11-06 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0013_transcription_annotator_id_alter_transcription_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcription',
            name='annotator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini.annotator'),
        ),
    ]