from django.contrib import admin
from .models import Artista, Album, Cancion

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "genero")
    search_fields = ("nombre", "pais", "genero")
    list_filter = ("pais", "genero")

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "fecha_lanzamiento", "num_canciones", "es_explicit", "usuario")
    list_filter = ("artista", "es_explicit", "fecha_lanzamiento")
    search_fields = ("titulo",)
    autocomplete_fields = ("artista", "usuario")

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "album", "duracion")
    list_filter = ("album",)
    search_fields = ("titulo",)
    autocomplete_fields = ("album",)