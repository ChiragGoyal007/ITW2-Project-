# Generated by Django 4.2.6 on 2023-11-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_song_album_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(max_length=50),
        ),
    ]