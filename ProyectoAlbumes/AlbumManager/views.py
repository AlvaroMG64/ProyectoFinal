from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm

# -------------------
# Artista Views
# -------------------
@login_required
def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, "artistas/lista.html", {"artistas": artistas})

@login_required
def crear_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_artistas")
    else:
        form = ArtistaForm()
    return render(request, "artistas/form.html", {"form": form, "accion": "Crear"})

@login_required
def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect("lista_artistas")
    else:
        form = ArtistaForm(instance=artista)
    return render(request, "artistas/form.html", {"form": form, "accion": "Editar"})

@login_required
def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        artista.delete()
        return redirect("lista_artistas")
    return render(request, "artistas/confirmar_eliminar.html", {"obj": artista})

# -------------------
# Album Views
# -------------------
@login_required
def lista_albumes(request):
    albumes = Album.objects.filter(usuario=request.user)
    return render(request, "albumes/lista.html", {"albumes": albumes})

@login_required
def crear_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.usuario = request.user
            album.save()
            return redirect("lista_albumes")
    else:
        form = AlbumForm()
    return render(request, "albumes/form.html", {"form": form, "accion": "Crear"})

@login_required
def editar_album(request, pk):
    album = get_object_or_404(Album, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("lista_albumes")
    else:
        form = AlbumForm(instance=album)
    return render(request, "albumes/form.html", {"form": form, "accion": "Editar"})

@login_required
def eliminar_album(request, pk):
    album = get_object_or_404(Album, pk=pk, usuario=request.user)
    if request.method == "POST":
        album.delete()
        return redirect("lista_albumes")
    return render(request, "albumes/confirmar_eliminar.html", {"obj": album})

# -------------------
# Cancion Views
# -------------------
@login_required
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, "canciones/lista.html", {"canciones": canciones})

@login_required
def crear_cancion(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_canciones")
    else:
        form = CancionForm()
    return render(request, "canciones/form.html", {"form": form, "accion": "Crear"})

@login_required
def editar_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect("lista_canciones")
    else:
        form = CancionForm(instance=cancion)
    return render(request, "canciones/form.html", {"form": form, "accion": "Editar"})

@login_required
def eliminar_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        cancion.delete()
        return redirect("lista_canciones")
    return render(request, "canciones/confirmar_eliminar.html", {"obj": cancion})