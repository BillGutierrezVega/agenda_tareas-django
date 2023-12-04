from django.shortcuts import render

from .forms import TareaForm

# Create your views here.
def crear_tarea(request):
    ruta_crea = 'templates_tareas/crear_tarea.html'
    if request.method == 'POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = TareaForm(initial={
                'nombre': '',
                'descripcion_corta': '',
                'descripcion': '',
                'fecha_limite': ''
            })
            mensaje = 'Datos guardados correctamente'
            return render(request, ruta_crea, {'formulario':formulario, 'mensaje':mensaje})
    else:
        formulario = TareaForm()
    return render(request, ruta_crea, {'formulario':formulario})


def cam(request):
    return render(request, '', {})


def cam(request):
    return render(request, '', {})


def cam(request):
    return render(request, '', {})


def cam(request):
    return render(request, '', {})