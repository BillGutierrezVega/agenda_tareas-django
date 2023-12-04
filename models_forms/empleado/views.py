from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmpleadoForm

# Create your views here.
def empleado(request):
    empleado = EmpleadoForm()
    return render(request, 'empleado.html', {'empleado':empleado})