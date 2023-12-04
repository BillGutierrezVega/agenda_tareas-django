from django.shortcuts import render

from .models import Personabien

def form(request):
    return render(request, 'form.html', {})

def goal(request):
    name = request.POST.get('name2')
    comentarios = request.POST.get('coment')
    persona = Personabien(nombre=name,  comentario=comentarios)
    persona.save()
    
    lista = Personabien.objects.all()
    
    return render(request, 'confirmado.html', {'name':name, 'lista':lista})