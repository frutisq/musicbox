# Generated by Django 5.0.7 on 2024-09-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_album_year_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
