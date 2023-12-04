from django.shortcuts import render
from django.http import HttpResponse

from .models import Reporter, Article

# Create your views here.
def many(_request):
    reporter = Reporter(first_name='bill3', last_name='guti3', email='bill3@gmail.com')
    reporter.save()
    
    article3 = Article(headline='primer articulo3', reporter=reporter)
    article3.save()
    
    article4 = Article(headline='segundo articulo3', reporter=reporter)
    article4.save()
    
    # result = article1.reporter.first_name
    result2 = reporter.article_set.all()
    return HttpResponse(result2)