from django.db import models
from django.contrib.auth.models import User

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50,default="España")
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    es_explicit = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def num_canciones(self):
        return self.cancion_set.count()

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duracion = models.IntegerField(help_text="Duración en segundos")

    def __str__(self):
        return self.titulo