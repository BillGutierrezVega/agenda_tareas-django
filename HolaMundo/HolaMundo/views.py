from django.http import HttpResponse

def saludo(_request):
    return HttpResponse("Hola mundo")

def despedida(_request):
    return HttpResponse("Adiós payasos")

def identificacion(_request, id):
    return HttpResponse(f'El id del alumno es: {id}')

def identificacion2(_request):
    return HttpResponse('Ingrese el id del alumno')