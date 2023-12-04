from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.
def stok(request):
    if request.method == 'POST':
        stok = ProductForm(request.POST)
        if stok.is_valid():
            stok.save()
            name = request.POST.get('name')
            return render(request, 'registro.html', {'name':name})
    if request.method == 'GET':
        stok = ProductForm()
        return render(request, 'stok.html', {'stok':stok})
        
def registro(request):
    
    return render(request, 'registro.html')