
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cancionero/', views.cancionero, name='cancionero'),
    path('biblia/', views.biblia, name='biblia'),
    path('miembros/', views.miembros, name='miembros'),
    
]
