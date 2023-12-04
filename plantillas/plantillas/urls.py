
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', views.simple, name='simple'),
    path('despedida/', views.despedida, name='despedida'),
    path('dinamico/<str:nombre>/', views.dinamico, name='dinamico'),
    path('identificacion/<int:id>/', views.identificar, name='identificar'),
    path('datos/<str:nombre>/<str:apellido>/<int:edad>/', views.datosalumnos, name='datosalumno')
]
