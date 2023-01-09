from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Album, Song, Artist
from .forms import AlbumForm
import json

# Create your views here.
# this is where actions happen. they are triggered by the user (or an AJAX request) visiting a url


def index(request):
    albums = Album.objects.all()
    form = AlbumForm()
    context = {
        'form': form,
        'albums': albums,
    }
    return render(request, 'music/index.html', context)


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            album = form.save(commit=False)
            # commit is false to hold off on DB until additional info added
            album.owner = request.user
            album.save()
            return redirect('home')
    data = {
        'created': 'yes'
    }
    return JsonResponse(data)
