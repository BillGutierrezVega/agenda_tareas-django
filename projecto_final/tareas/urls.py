from django.urls import path

from . import views

urlpatterns = [
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('borrar_tareas/', views.borrar_tareas, name='borrar_tareas'),
    path('buscar_tareas/', views.buscar_tareas, name='buscar_tareas'),
    path('editar_tareas/', views.editar_tareas, name='editar_tareas'),
]