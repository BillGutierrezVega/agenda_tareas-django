from django.shortcuts import render, redirect

from .forms import ContactosForm, FormularioMulti
from .models import Contactos

# Create your views here.
def agenda_crear(request):
    if request.method == 'POST':
        creando_contacto = ContactosForm(request.POST)
        if creando_contacto.is_valid():
            creando_contacto.save()
            creando_contacto = ContactosForm(initial={
                'nombre':'',
                'apellido':'',
                'email':'',
                'celular':'',
                'direccion':''
            })
            context = {
                'mensaje':'Datos guardados exitosamente',
                'creando_contacto':creando_contacto
            }
            return render(request, 'templates_agenda/agenda_crear.html', context)

    creando_contacto = ContactosForm()
    return render(request, 'templates_agenda/agenda_crear.html', {'creando_contacto':creando_contacto})


def agenda_borrar(request):
    if request.method == 'GET':
        form_borrar = FormularioMulti()
        return render(request, 'templates_agenda/agenda_borrar.html', {'form_borrar':form_borrar})
    if request.method == 'POST':
        form_borrar = FormularioMulti(request.POST)
        if form_borrar.is_valid():
            nombre = request.POST.get('nombre')
            borrar = Contactos.objects.filter(nombre=nombre).first()
            borrar.delete()
            context = {
                    'mensaje':'Datos eliminados exitosamente'
                }
            return render(request, 'templates_agenda/agenda_borrar.html', context)


def agenda_listar(request):
    lista = Contactos.objects.all()
    return render(request, 'templates_agenda/agenda_listar.html', {'lista':lista})


def agenda_editar(request):
    ruta = 'templates_agenda/agenda_editar.html'
    if request.method == 'GET':
        formulario_busqueda = FormularioMulti()
        return render(request, ruta, {'formulario_busqueda': formulario_busqueda})
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = Contactos.objects.filter(nombre=nombre).first()

        if contacto:
            formulario = ContactosForm(request.POST, instance=contacto)
            if formulario.is_valid():
                formulario.save()
                return redirect('agenda_editar')
        else:
            # Manejar el caso en el que no se encuentra el objeto Contactos
            return render(request, ruta, {'formulario_busqueda': FormularioMulti(), 'formulario': None})

        return render(request, ruta, {'formulario_busqueda': FormularioMulti(), 'formulario': formulario})


def agenda_buscar(request):
    if request.method == 'GET':
        formulario_busqueda = FormularioMulti()
        return render(request, 'templates_agenda/agenda_buscar.html', {'formulario_busqueda':formulario_busqueda})
    
    if request.method == 'POST':
        formulario_busqueda = FormularioMulti(request.POST)
        if formulario_busqueda.is_valid():
            nombre = request.POST.get('nombre')
            encontrados = Contactos.objects.filter(nombre=nombre)
            return render(request, 'templates_agenda/agenda_buscar.html', {'encontrados':encontrados})

