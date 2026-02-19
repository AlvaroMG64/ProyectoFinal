from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Artista, Cancion
from .forms import AlbumForm, ArtistaForm, CancionForm
from django.utils import timezone

# ---------------- DASHBOARD ----------------

@login_required
def dashboard(request):
    usuario = request.user
    hora_actual = timezone.localtime(timezone.now())  # Fecha y hora actual localizable
    mensaje_reglas = [
        "Un álbum no puede tener más de 20 canciones.",
        "Un artista no puede lanzar más de 2 álbumes en el mismo año.",
        "Eliminar un álbum eliminará sus canciones asociadas."
    ]
    return render(request, "dashboard.html", {
        "usuario": usuario,
        "hora_actual": hora_actual,
        "mensaje_reglas": mensaje_reglas
    })

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
        album.delete()  # Cascada borrará canciones asociadas
        return redirect("lista_albumes")
    mensaje_cascada = "Si eliminas este álbum, se borrarán todas las canciones asociadas."
    return render(request, "albumes/confirmar_eliminar.html", {
        "album": album,
        "mensaje_cascada": mensaje_cascada
    })

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
        artista.delete()  # Cascada borrará álbumes y canciones asociadas
        return redirect("lista_artistas")
    mensaje_cascada = (
        "Si eliminas este artista, se borrarán todos sus álbumes "
        "y las canciones asociadas a esos álbumes."
    )
    return render(request, "artistas/confirmar_eliminar.html", {
        "artista": artista,
        "mensaje_cascada": mensaje_cascada
    })

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
    # Normalmente borrar una canción no afecta nada más, pero dejamos mensaje opcional
    mensaje_cascada = "Si eliminas esta canción, se eliminará permanentemente del álbum."
    return render(request, "canciones/confirmar_eliminar.html", {
        "cancion": cancion,
        "mensaje_cascada": mensaje_cascada
    })