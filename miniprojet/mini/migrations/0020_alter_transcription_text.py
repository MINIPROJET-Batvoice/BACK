# Generated by Django 4.2.7 on 2023-11-08 23:46

from django.db import migrations, models
import mini.validator


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0019_delete_annotator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcription',
            name='text',
            field=models.TextField(validators=[mini.validator.TextValidator]),
        ),
    ]
