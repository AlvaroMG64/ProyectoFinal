from django import forms
from .models import Artista, Album, Cancion

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ["nombre", "pais", "genero"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["titulo", "artista", "fecha_lanzamiento", "es_explicit"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.Select(attrs={'class': 'form-select'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'es_explicit': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')]),
        }

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ["titulo", "album", "duracion"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-select'}),
            'duracion': forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
        }