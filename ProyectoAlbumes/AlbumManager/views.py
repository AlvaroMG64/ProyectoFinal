from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Cancion
from .forms import AlbumForm, CancionForm

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