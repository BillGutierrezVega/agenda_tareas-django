from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def cancionero(request):
    return render(request, 'cancionero.html', {})

def biblia(request):
    return render(request, 'biblia.html', {})

def miembros(request):
    return render(request, 'miembros.html', {})
