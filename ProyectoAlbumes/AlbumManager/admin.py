from django.contrib import admin
from .models import Artista, Album, Cancion

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'fecha_lanzamiento', 'num_canciones', 'es_explicit', 'usuario')
    list_filter = ('artista', 'fecha_lanzamiento', 'es_explicit')

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracion')
    list_filter = ('album',)