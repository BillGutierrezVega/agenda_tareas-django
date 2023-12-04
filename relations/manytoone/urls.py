from django.urls import path

from . import views

urlpatterns = [
    path('many/', views.many, name='many'),
]
