from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('producto/', views.producto, name='producto'),
    path('producto_registrado/', views.producto_registrado, name='producto_registrado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)