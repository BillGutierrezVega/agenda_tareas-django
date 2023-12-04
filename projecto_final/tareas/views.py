from django.shortcuts import render

from .forms import TareaForm, BusquedaForm
from .models import Tarea

# Create your views here.
def crear_tarea(request):
    ruta_crea = 'templates_tareas/crear_tarea.html'
    formulario = TareaForm(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            formulario = TareaForm(initial={
                'nombre': '',
                'descripcion_corta': '',
                'descripcion': '',
                'fecha_limite': ''
            })
            
            mensaje = 'Datos guardados correctamente'
            
            lista_tareas = Tarea.objects.all()
            
            context = {
                'mensaje':mensaje,
                'formulario': formulario,
                'lista_tareas': lista_tareas
            }
            return render(request, ruta_crea, context)
    else:
        formulario = TareaForm()
        lista_tareas = Tarea.objects.all()
        context = {
            'formulario': formulario,
            'lista_tareas': lista_tareas
        }
    return render(request, ruta_crea, context)


def borrar_tareas(request):
    ruta = 'templates_tareas/borrar_tareas.html'
    if request.method == 'POST':
        busqueda = BusquedaForm(request.POST)
        if busqueda.is_valid():
            nombre = busqueda.cleaned_data['nombre']
            borra = Tarea.objects.filter(nombre=nombre).first()
            
            if borra:
                borra.delete()
                busqueda = BusquedaForm(initial={
                    'nombre':''
                })
                mensaje = 'Borrado de datos exitoso!!'
                return render(request, ruta, {'mensaje':mensaje, 'busqueda':busqueda})
            else:
                busqueda = BusquedaForm()
                mensaje = 'Datos inválidos!!'
                return render(request, ruta, {'mensaje':mensaje, 'busqueda':busqueda})
        
    busqueda = BusquedaForm()
    return render(request, ruta, {'busqueda':busqueda})


def buscar_tareas(request):
    ruta = 'templates_tareas/buscar_tareas.html'
    if request.method == 'POST':
        formulario = BusquedaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            busqueda = Tarea.objects.filter(nombre=nombre)
            if busqueda:
                return render(request, ruta, {'formulario':formulario, 'busqueda':busqueda})
            else:
                mensaje = 'Datos no encontrados'
                return render(request, ruta, {'formulario':formulario, 'mensaje':mensaje})
            
    formulario = BusquedaForm()
    return render(request, ruta, {'formulario':formulario})


def editar_tareas(request):
    ruta = 'templates_tareas/editar_tareas.html'
    
    if request.method == 'POST':
        formulario_buscar = BusquedaForm(request.POST)
        
        if formulario_buscar.is_valid():
            nombre = formulario_buscar.cleaned_data['nombre']
            encuentra_nombre = Tarea.objects.filter(nombre=nombre).first()
            
            if encuentra_nombre:
                tareas = TareaForm(request.POST, instance=encuentra_nombre)
                
                if tareas.is_valid():
                    tareas.save()
                    return render(request, ruta, {'tareas': tareas})
            else:
                mensaje = 'Datos no encontrados'
                tareas = TareaForm()
                return render(request, ruta, {'mensaje': mensaje, 'tareas': tareas})
    
    formulario_buscar = BusquedaForm()
    tareas = TareaForm()    
    return render(request, ruta, {'formulario_buscar': formulario_buscar, 'tareas': tareas})
