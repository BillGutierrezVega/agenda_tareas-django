from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cliente, Canciones, Playlist

# Create your views here.
def cliente(request):
    if request.method == 'POST':
        nombre_cli = request.POST.get('nombre')
        edad = request.POST.get('edad')
        dni = request.POST.get('dni')
        
        cliente = Cliente(nombre = nombre_cli, edad=edad, dni=dni)
        cliente.save()
        
        result = Cliente.objects.all()
        
        return render(request, 'cliente_confirmado.html', {"result":result})
    else:
        return render(request, "cliente.html")
    
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'detalle_cliente.html', {"cliente":cliente})

def cliente_confirmado(request):
    #result = Cliente.objects.all()
    return render(request, 'cliente_confirmado.html', {})


def canciones(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        letras = request.POST.get('letras')
        
        salvar = Canciones(nombre=nombre, letras=letras)
        salvar.save()
        
        cancion = Canciones.objects.all()
        
        return render(request, 'canciones_confirmacion.html', {'cancion': cancion})
    else:
        return render(request, 'canciones.html')

def canciones_confirmacion(request):
    cancion = Canciones.objects.all()
    return render(request, 'canciones_confirmacion.html', {'cancion': cancion})

def detalles_cancion(request, id_cancion):
    cancion = get_object_or_404(Canciones, id=id_cancion)
    return render(request, 'detalles_cancion.html', {'cancion': cancion})


def inicio(request):
    return render(request, 'inicio.html', {})


def playlist(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_playlist')
        cli = request.POST.get('nombre_cliente')
        cliente = Cliente.objects.get(nombre=cli)
        can = request.POST.get('nombre_cancion')
        cancion = Canciones.objects.get(nombre=can)

        # Verificar si ya existe una playlist con el mismo nombre y cliente
        playlist_existente = Playlist.objects.filter(nombre=nombre, cliente=cliente).first()

        if playlist_existente:
            # Agregar canción a la playlist existente
            playlist_existente.cancion.add(cancion)
        else:
            # Crear una nueva playlist
            playlist_nueva = Playlist(nombre=nombre, cliente=cliente)
            playlist_nueva.save()
            playlist_nueva.cancion.add(cancion)

        play = Playlist.objects.all()
        return render(request, 'playlist_confirmacion.html', {'play': play})
    else:
        return render(request, 'playlist.html', {}) 
    
def playlist_confirmacion(request):
    return render(request, 'playlist_confirmacion.html', {})
