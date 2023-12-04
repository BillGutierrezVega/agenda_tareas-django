from django.shortcuts import render

from .models import Author, Entry

# Create your views here.
def querris(request):
    # Trayebdo todos los objetos 
    authors = Author.objects.all()
    
    # Filtrando una consulta
    filtrado = Author.objects.filter(email='melissa23@example.com')
    
    # Filtrado pero solo obtener un elemento
    author = Author.objects.get(id=1)
    
    # Obtener los 10 elementos
    limit = Author.objects.all()[:10]
    
    # Obtener los 5 elementos saltando 5
    ofset = Author.objects.all()[5:10]
    
    # Totalidad de elementos ordenados
    ordenados = Author.objects.all().order_by("email")
    
    # Obtener los registros con ID menor igual a 15
    filter2 = Author.objects.filter(id__lte = 15)
    
    # Obtener los registros que contengan "get"
    woman = Author.objects.filter(name__contains = "get")
    
    return render(request, 'post/queries.html', {'authors':authors, 'filtrado':filtrado, 'author':author, 'limit':limit, 'ofset':ofset, 'ordenados':ordenados, 'filter2':filter2, 'woman':woman})

def update(request, id):
    actualiza1 = Author.objects.get(id=id)
    actualiza1.name = "bill gutierrez"
    actualiza1.save()
    return render(request, 'post/update.html', {})