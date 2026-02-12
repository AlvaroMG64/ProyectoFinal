from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Artista, Cancion
from .forms import AlbumForm, ArtistaForm, CancionForm

# -------------------------
# ARTISTAS
# -------------------------
@login_required
def artista_list(request):
    artistas = Artista.objects.all()
    return render(request, 'artista_list.html', {'artistas': artistas})

@login_required
def artista_create(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artista_list')
    else:
        form = ArtistaForm()
    return render(request, 'artista_form.html', {'form': form, 'accion': 'Crear'})

@login_required
def artista_edit(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artista_list')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artista_form.html', {'form': form, 'accion': 'Editar'})

@login_required
def artista_delete(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('artista_list')
    return render(request, 'artista_confirm_delete.html', {'artista': artista})

# -------------------------
# ALBUMES
# -------------------------
@login_required
def album_list(request):
    albums = Album.objects.filter(usuario=request.user)
    return render(request, 'album_list.html', {'albumes': albums})

@login_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.usuario = request.user
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form, 'accion': 'Crear'})

@login_required
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form, 'accion': 'Editar'})

@login_required
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk, usuario=request.user)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'album_confirm_delete.html', {'album': album})

# -------------------------
# CANCIONES
# -------------------------
@login_required
def cancion_list(request):
    canciones = Cancion.objects.filter(album__usuario=request.user)
    return render(request, 'cancion_list.html', {'canciones': canciones})

@login_required
def cancion_create(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cancion_list')
    else:
        form = CancionForm()
    return render(request, 'cancion_form.html', {'form': form, 'accion': 'Crear'})

@login_required
def cancion_edit(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk, album__usuario=request.user)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('cancion_list')
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'cancion_form.html', {'form': form, 'accion': 'Editar'})

@login_required
def cancion_delete(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk, album__usuario=request.user)
    if request.method == 'POST':
        cancion.delete()
        return redirect('cancion_list')
    return render(request, 'cancion_confirm_delete.html', {'cancion': cancion})