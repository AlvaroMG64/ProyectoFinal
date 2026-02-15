from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Artista, Cancion
from .forms import AlbumForm, ArtistaForm, CancionForm
from django.utils.timezone import localtime, now

# ---------------- DASHBOARD ----------------

@login_required
def dashboard(request):
    context = {"now": now()}
    return render(request, "dashboard.html", context)


# ---------------- ÁLBUMES ----------------

@login_required
def lista_albumes(request):
    albumes = Album.objects.all()
    return render(request, "albumes/lista.html", {"albumes": albumes})


@login_required
def crear_album(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_albumes")
    return render(request, "albumes/form.html", {"form": form, "accion": "Crear"})


@login_required
def editar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect("lista_albumes")
    return render(request, "albumes/form.html", {"form": form, "accion": "Editar"})


@login_required
def eliminar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect("lista_albumes")
    return render(request, "albumes/confirmar_eliminar.html", {"album": album})


# ---------------- ARTISTAS ----------------

@login_required
def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, "artistas/lista.html", {"artistas": artistas})


@login_required
def crear_artista(request):
    form = ArtistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_artistas")
    return render(request, "artistas/form.html", {"form": form, "accion": "Crear"})


@login_required
def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    form = ArtistaForm(request.POST or None, instance=artista)
    if form.is_valid():
        form.save()
        return redirect("lista_artistas")
    return render(request, "artistas/form.html", {"form": form, "accion": "Editar"})


@login_required
def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        artista.delete()
        return redirect("lista_artistas")
    return render(request, "artistas/confirmar_eliminar.html", {"artista": artista})


# ---------------- CANCIONES ----------------

@login_required
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, "canciones/lista.html", {"canciones": canciones})


@login_required
def crear_cancion(request):
    form = CancionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_canciones")
    return render(request, "canciones/form.html", {"form": form, "accion": "Crear"})


@login_required
def editar_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    form = CancionForm(request.POST or None, instance=cancion)
    if form.is_valid():
        form.save()
        return redirect("lista_canciones")
    return render(request, "canciones/form.html", {"form": form, "accion": "Editar"})


@login_required
def eliminar_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        cancion.delete()
        return redirect("lista_canciones")
    return render(request, "canciones/confirmar_eliminar.html", {"cancion": cancion})