from django.contrib import admin
from .models import Artista, Album, Cancion

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais',)
    search_fields = ('nombre', 'pais',)
    list_filter = ('pais',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'fecha_lanzamiento', 'num_canciones', 'es_explicit', 'usuario')
    list_filter = ('fecha_lanzamiento', 'es_explicit')
    search_fields = ('titulo', 'artista__nombre',)
    autocomplete_fields = ('artista', 'usuario',)


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracion')
    search_fields = ('titulo', 'album__titulo',)
    autocomplete_fields = ('album',)