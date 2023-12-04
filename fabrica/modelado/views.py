from django.shortcuts import render
from django.http import HttpResponse

from .models import Salario, PuestoLaboral, Poblacion, FabricaLaboral, Empleado

# Create your views here.
def empleado(_request):
    salario = Salario(bruto_cobrar=2800.50, pago_extra=1)
    salario.save()
    
    poblacion = Poblacion(pais='Peru', departamentos='Lima')
    poblacion.save()
    
    puestolaboral = PuestoLaboral(nombre_cargo='Diseñador', descripcion='Es el que desarrolla las aplicaciones que todos usan en su vida diaria', salario=salario)
    puestolaboral.save()
    
    fabrica = FabricaLaboral(nombre_fabrica='Casa hogar', direccion='Prol. Julio Llanos # 661', cod_postal='0685478', poblacion=poblacion)
    fabrica.save()
    
    empleados = Empleado(nombre='Ana Gutierrez', dni='48459565', email="ana@hotmail.com", direccion='la misma que la fábrica', puesto_laboral=puestolaboral, fabrica_laboral=fabrica)
    empleados.save()
    
    result = Empleado.objects.get(nombre='Ana Gutierrez')
    return HttpResponse(result)

def filtrado(_request):
    empleados_peru = Empleado.objects.filter(fabrica_laboral__poblacion__pais='Peru')
    return HttpResponse(empleados_peru)