from django.contrib import admin
from .models import User, Song, Artist, Album

# Register your models here.
admin.site.register(User)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
