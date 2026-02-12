from django.db import models
from django.contrib.auth.models import User

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albumes')
    fecha_lanzamiento = models.DateField()
    num_canciones = models.PositiveIntegerField()
    es_explicit = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')

    def __str__(self):
        return self.titulo