from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def artists_from_songs(self):
        return [song.artist for song in self.songs.all()]


class Song(models.Model):
    HIP_HOP = 'HH'
    POP = 'PO'
    ROCK = 'RO'
    COUNTRY = 'CO'
    ALTERNATIVE = 'ALT'

    GENRE_CHOICES = [
        (HIP_HOP, 'Hip-Hop/Rap'),
        (POP, 'Pop'),
        (ROCK, 'Rock'),
        (COUNTRY, 'Country'),
        (ALTERNATIVE, 'Alternative'),
    ]

    name = models.CharField(max_length=50)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default=None, related_name='songs')
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, default=None, related_name='songs')

    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)

    def __str__(self):
        return f'{self.name} by {self.artist}'
