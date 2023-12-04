from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Publication

# Create your views here.
def create(_request):
    art1 = Article(headline='este es un headline1')
    art1.save()
    art2 = Article(headline='este es un headline2')
    art2.save()
    art3 = Article(headline='este es un headline3')
    art3.save()
    
    pub1 = Publication(title='nuevo titulo1')
    pub1.save()
    pub2 = Publication(title='nuevo titulo2')
    pub2.save()
    pub3 = Publication(title='nuevo titulo3')
    pub3.save()
    pub4 = Publication(title='nuevo titulo4')
    pub4.save()
    pub5 = Publication(title='nuevo titulo5')
    pub5.save()
    pub6 = Publication(title='nuevo titulo6')
    pub6.save()
    pub7 = Publication(title='nuevo titulo7')
    pub7.save()
    
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    
    result = art3.publications.all()
    
    # consultar del lado de las publicaciones
    # publi1 = Publication.objects.get(id=38)
    # result = publi1.article_set.all()
    
    # borrar datos de una tabla
    # borrar = Publication.objects.all()
    # borrar.delete()
    
    return HttpResponse(result)