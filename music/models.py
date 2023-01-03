from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


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
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    image = models.ImageField(blank=True, null=True)
