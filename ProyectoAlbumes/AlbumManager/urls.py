from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # Álbumes
    path("albumes/", views.lista_albumes, name="lista_albumes"),
    path("albumes/crear/", views.crear_album, name="crear_album"),
    path("albumes/editar/<int:pk>/", views.editar_album, name="editar_album"),
    path("albumes/eliminar/<int:pk>/", views.eliminar_album, name="eliminar_album"),

    # Artistas
    path("artistas/", views.lista_artistas, name="lista_artistas"),
    path("artistas/crear/", views.crear_artista, name="crear_artista"),
    path("artistas/editar/<int:pk>/", views.editar_artista, name="editar_artista"),
    path("artistas/eliminar/<int:pk>/", views.eliminar_artista, name="eliminar_artista"),

    # Canciones
    path("canciones/", views.lista_canciones, name="lista_canciones"),
    path("canciones/crear/", views.crear_cancion, name="crear_cancion"),
    path("canciones/editar/<int:pk>/", views.editar_cancion, name="editar_cancion"),
    path("canciones/eliminar/<int:pk>/", views.eliminar_cancion, name="eliminar_cancion"),
]