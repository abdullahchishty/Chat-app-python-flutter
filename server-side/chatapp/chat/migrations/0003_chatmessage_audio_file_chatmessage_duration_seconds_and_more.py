# Generated by Django 4.0.1 on 2024-03-26 05:47

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=chat.models.user_voicemessages_path),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='duration_seconds',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
