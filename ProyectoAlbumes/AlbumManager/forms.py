from django import forms
from .models import Album, Artista, Cancion

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'fecha_lanzamiento', 'num_canciones', 'es_explicit']

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'genero']

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'duracion', 'album']