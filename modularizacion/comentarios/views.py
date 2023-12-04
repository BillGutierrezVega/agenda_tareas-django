from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("Hola mundo")

def create(_request):
    comentario1 = Comment(name="comentario3", score=7, comment="este es un comentario el primero por cierto")
    comentario1.save()
    # comentario1 = Comment.objects.create(name="Bill") errorLens.disableLine
    return HttpResponse("para create")

def delete(_request):
    coment = Comment.objects.get(id=2)
    coment.delete()
    
    # Comment.objects.filter(id=3).delete()
    
    return HttpResponse("Prueba de borrado")