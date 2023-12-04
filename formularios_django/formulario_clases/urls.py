from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('comprueba/', views.comprueba, name='comprueba'),
    path('widget/', views.widget, name='widget'),
    path('contacto_confirma/', views.contacto_confirma, name='contacto_confirma'),
    path('profesor/', views.profesor, name='profesor'),
    path('alumnos/', views.alumnos, name='alumnos'),
]