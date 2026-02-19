from django import forms
from datetime import timedelta
from .models import Artista, Album, Cancion


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "genero": forms.TextInput(attrs={"class": "form-control"}),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "artista": forms.Select(attrs={"class": "form-select"}),
            "fecha_lanzamiento": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "num_canciones": forms.NumberInput(attrs={"class": "form-control"}),
            "es_explicit": forms.RadioSelect(choices=[(True, "Sí"), (False, "No")]),
            "usuario": forms.Select(attrs={"class": "form-select"}),
        }


class CancionForm(forms.ModelForm):
    duracion = forms.CharField(
        label="Duración (MM:SS)",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ej. 03:45"})
    )

    class Meta:
        model = Cancion
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "album": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_duracion(self):
        data = self.cleaned_data['duracion']
        try:
            minutos, segundos = map(int, data.split(":"))
            return timedelta(minutes=minutos, seconds=segundos)
        except Exception:
            raise forms.ValidationError("Introduce la duración en formato MM:SS")