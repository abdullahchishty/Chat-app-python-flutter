# Generated by Django 5.0.3 on 2024-03-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='request_sent',
            field=models.BooleanField(default=False),
        ),
    ]