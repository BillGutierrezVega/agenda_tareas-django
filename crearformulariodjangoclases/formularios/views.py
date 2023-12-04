from django.shortcuts import render

from .forms import FormularioUsuario

# Create your views here.
def formulario(request):
    usuario = FormularioUsuario()
    return render (request, 'formulario.html', {'usuario': usuario})

def datos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        dni = request.POST.get('dni')
        context = {
            'nombre':nombre,
            'apellido':apellido,
            'edad':edad,
            'dni':dni
        }
        return render(request, 'datos.html', context)
    return render (request, 'formulario.html')