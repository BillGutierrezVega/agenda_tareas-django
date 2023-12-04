from django.http import HttpResponse
from django.shortcuts import render

def simple(request):
    return render(request, 'saludo.html', {})

def despedida(request):
    datos = {
        "nombre":'bill',
        "apellido":'guti'
    }
    return render(request, 'despedida.html', datos)

def dinamico(request, nombre):
    contexto = {
        'nombre':nombre
    }
    return render(request, 'dinamico.html', contexto)

def identificar(request, id):
    categorias = ['desarrollador', 'analista', 'diseñador']
    context = {
        'id': id,
        'categorias':categorias
    }
    return render(request, 'identificacion.html', context)

def datosalumnos(request, nombre, apellido, edad):
    cursos = ['Algebra', 'Química', 'Física', 'Aritmetica']
    context = {
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
        'cursos':cursos
    }
    return render(request, 'datosalumno.html', context)