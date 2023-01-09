from django import forms
from .models import Song, Album, Artist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('name', 'release_date',)
