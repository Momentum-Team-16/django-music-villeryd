from django.shortcuts import render
from .models import Album, Song, Artist
import json

# Create your views here.
# this is where actions happen. they are triggered by the user (or an AJAX request) visiting a url


def index(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'music/index.html', context)


def parse_song():
    breakpoint()
    with open('music/test.json') as file:
        data = json.load(file)
        print(f"{type(data)} \n\n {data}")

    album = Album.objects.create(name=data.get('collectionName'), owner_id=1)
    artist = Artist.objects.create(name=data.get('artistName'))
    song = Song.objects.create(name=data.get("trackName"),
                               album=album,
                               genre='PO',
                               artist=artist)

    print(f'\n{song}')
