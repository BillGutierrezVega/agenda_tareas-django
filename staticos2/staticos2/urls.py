
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estaticos2/', views.estaticos2, name='estaticos2'),
]
