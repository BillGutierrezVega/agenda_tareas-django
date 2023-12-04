from django.urls import path

from . import views

urlpatterns = [
    path('empleado/', views.empleado, name='empleado'),
    path('filtrado/', views.filtrado, name='filtrado'),
]
