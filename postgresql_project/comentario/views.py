from django.shortcuts import render
from django.http import HttpResponse

from .models import Comentarios, Author

# Create your views here.
def comenta(_request):
    autor2 = Author(name='velentina', email='vale@example.net')
    autor2.save()
    
    comentario1 = Comentarios(comenta='este es un comentario10', ratings=5, author=autor2)
    comentario1.save()
    comentario2 = Comentarios(comenta='este es un comentario20', ratings=2, author=autor2)
    comentario2.save()
    comentario3 = Comentarios(comenta='este es un comentario30', ratings=7, author=autor2)
    comentario3.save()
    comentario4 = Comentarios(comenta='este es un comentario40', ratings=7, author=autor2)
    comentario4.save()
    comentario5 = Comentarios(comenta='este es un comentario50', ratings=7, author=autor2)
    comentario5.save()
    
    return HttpResponse('Creado con éxito')

def filtros(_request):
    autor = Author.objects.get(id=2)
    # result = autor.comentarios_set.all()
    comentarios_del_autor = [comentario.comenta for comentario in autor.comentarios_set.all()]
    result = ', '.join(comentarios_del_autor)

    return HttpResponse(result)

def filtros2(_request):
    # comenta1 = Comentarios.objects.get(id=4)
    # result = comenta1.author.email
    rating = Comentarios.objects.filter(ratings=7)
    return HttpResponse(rating)