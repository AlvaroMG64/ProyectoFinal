from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    es_explicit = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def num_canciones(self):
        """Número de canciones asociadas."""
        return self.cancion_set.count()
    num_canciones.fget.short_description = "Nº Canciones"

    def clean(self):
        """Reglas de negocio: máximo 20 canciones, máximo 2 álbumes por año por artista."""
        # Regla: máximo 20 canciones (solo si hay canciones existentes)
        if self.pk and self.cancion_set.count() > 20:
            raise ValidationError("Un álbum no puede tener más de 20 canciones.")

        # Regla: máximo 2 álbumes por artista en el mismo año
        if self.fecha_lanzamiento:
            año = self.fecha_lanzamiento.year
            albums_mismo_año = Album.objects.filter(
                artista=self.artista,
                fecha_lanzamiento__year=año
            )
            if self.pk:
                albums_mismo_año = albums_mismo_año.exclude(pk=self.pk)
            if albums_mismo_año.count() >= 2:
                raise ValidationError(
                    "Un artista no puede lanzar más de 2 álbumes en el mismo año."
                )

    def __str__(self):
        return self.titulo


class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo