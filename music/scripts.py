import models
from models import Song, Album, Artist
import json
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


with open('music/test.json') as file:
    data = json.load(file)
    print(f"{type(data)} \n\n {data}")

song = models.Song.objects.create(name=data.get("trackName"),
                                  album=data.get('collectionName'),
                                  genre=data.get('"primaryGenreName"'),
                                  artist='2')

print(f'\n{song}')
