# Generated by Django 5.0.7 on 2024-07-25 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='albums')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='main.section')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('lyrics', models.TextField(blank=True)),
                ('translate_lyrics', models.TextField(blank=True)),
                ('audio_file', models.FileField(blank=True, upload_to='audio/')),
                ('video_url', models.URLField(blank=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main.album')),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main.section')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
    ]
