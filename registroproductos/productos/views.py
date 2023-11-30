from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

def producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            # No necesitas extraer manualmente los campos del formulario, puedes usar cleaned_data directamente
            producto_form.save()
            todostodos_producto = Producto.objects.all()
            context = {'todo': todostodos_producto}
            return render(request, 'producto_registrado.html', context)
    else:
        producto_form = ProductoForm()

    return render(request, 'productos.html', {'producto_form': producto_form})

def producto_registrado(request):
    todostodos_producto = Producto.objects.all()
    context = {'todo': todostodos_producto}
    return render(request, 'producto_registrado.html', context)
