from django import forms
from .models import Album, Cancion

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'genero', 'fecha_lanzamiento', 'num_canciones', 'es_explicit']

    def clean_num_canciones(self):
        num = self.cleaned_data.get('num_canciones')
        if num < 1:
            raise forms.ValidationError("Un álbum debe tener al menos 1 canción")
        return num

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'duracion', 'album']

    def clean_duracion(self):
        dur = self.cleaned_data.get('duracion')
        if dur <= 0:
            raise forms.ValidationError("La duración debe ser positiva")
        return dur