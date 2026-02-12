from django.urls import path
from . import views

urlpatterns = [
    # ARTISTAS
    path('artistas/', views.artista_list, name='artista_list'),
    path('artistas/create/', views.artista_create, name='artista_create'),
    path('artistas/edit/<int:pk>/', views.artista_edit, name='artista_edit'),
    path('artistas/delete/<int:pk>/', views.artista_delete, name='artista_delete'),

    # ALBUMES
    path('', views.album_list, name='album_list'),
    path('albums/create/', views.album_create, name='album_create'),
    path('albums/edit/<int:pk>/', views.album_edit, name='album_edit'),
    path('albums/delete/<int:pk>/', views.album_delete, name='album_delete'),

    # CANCIONES
    path('canciones/', views.cancion_list, name='cancion_list'),
    path('canciones/create/', views.cancion_create, name='cancion_create'),
    path('canciones/edit/<int:pk>/', views.cancion_edit, name='cancion_edit'),
    path('canciones/delete/<int:pk>/', views.cancion_delete, name='cancion_delete'),
]