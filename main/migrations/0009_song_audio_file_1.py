# Generated by Django 5.1.1 on 2024-09-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_song_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file_1',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]
