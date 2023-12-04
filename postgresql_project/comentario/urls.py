from django.urls import path

from . import views

urlpatterns = [
    path('com/', views.comenta, name='comenta'),
    path('filtros/', views.filtros, name='filtros'),
    path('filtros2/', views.filtros2, name='filtros2'),
]
