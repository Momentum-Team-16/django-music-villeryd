from django.shortcuts import render

# Create your views here.
# this is where actions happen. they are triggered by the user (or an AJAX request) visiting a url


def index(request):
    context = {}
    return render(request, 'music/index.html', context)
