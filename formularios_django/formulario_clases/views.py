from django.shortcuts import render
from django.http import HttpResponse

from .forms import CommentsForm, ContactForm, Profesor, AlumnosForm

# Create your views here.
def form(request):
    comment_form = CommentsForm()
    return render(request, 'form.html', {'comment_form':comment_form})

def comprueba(request):
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            name = request.POST.get('name')
            url = request.POST.get('url')
            comment = request.POST.get('comment')
            context = {
                'name':name,
                'url':url,
                'comment':comment
            }
            return render(request, 'comprueba.html', context)
    else:
        comment_form = CommentsForm()
    return render(request, 'form.html', {'comment_form':comment_form})


def widget(request):
    contacto = ContactForm()
    return render(request, 'contacto.html', {'contacto':contacto})

def contacto_confirma(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        context = {
            'name':name,
            'email':email,
            'message':message
        }
        return render(request, 'contacto_confirma.html', context)
    return render(request, 'contacto.html')

def profesor(request):
    if request.method == 'GET':
        profesor = Profesor()
        return render(request ,'profesor.html', {'profesor':profesor})
    if request.method == 'POST':
        profesor = Profesor(request.POST)
        if profesor.is_valid():
            return HttpResponse('es valido')
        else:
            return render(request ,'profesor.html', {'profesor':profesor})
            # error_messages = '<br>'.join([f"{field}: {', '.join(errors)}" for field, errors in profesor.errors.items()])
            # return HttpResponse(f'El formulario no es válido. Errores:<br>\n{error_messages}')
            

def alumnos(request):
    if request.method == 'POST':
        alumno_form = AlumnosForm(request.POST)
        if alumno_form.is_valid():
            nombre = request.POST.get('nombre')
            edad = request.POST.get('edad')
            context = {
                'nombre':nombre,
                'edad':edad
            }
            return render(request, 'confirma_alumno.html', context)
    else:
        alumno_form = AlumnosForm()
    return render(request, 'formulario_alumno.html', {'alumno_form':alumno_form})