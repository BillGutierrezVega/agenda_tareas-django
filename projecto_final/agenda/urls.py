from django.urls import path

from . import views

urlpatterns = [
    path('agenda_crear/', views.agenda_crear, name='agenda_crear'),
    path('agenda_borrar/', views.agenda_borrar, name='agenda_borrar'),
    path('agenda_listar/', views.agenda_listar, name='agenda_listar'),
    path('agenda_editar/', views.agenda_editar, name='agenda_editar'),
    path('agenda_buscar/', views.agenda_buscar, name='agenda_buscar'),
]