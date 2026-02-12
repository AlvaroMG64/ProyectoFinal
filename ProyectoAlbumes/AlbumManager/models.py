from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    num_canciones = models.PositiveIntegerField()
    es_explicit = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en segundos")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="canciones")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.album.titulo})"