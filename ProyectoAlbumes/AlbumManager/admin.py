from django.contrib import admin
from .models import Artista, Album, Cancion

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Cancion)