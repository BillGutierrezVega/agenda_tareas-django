from django.urls import path

from . import views

urlpatterns = [
    path('cliente/', views.cliente, name='cliente'),
    path('cliente_confirmado/', views.cliente_confirmado, name='cliente_confirmado'),
    path('detalle_cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('canciones/', views.canciones, name='canciones'),
    path('canciones_confirmacion/', views.canciones_confirmacion, name='canciones_confirmacion'),
    path('detalles_cancion/<int:id_cancion>', views.detalles_cancion, name='detalles_cancion'),
    path('inicio/', views.inicio, name='inicio'),
    path('playlist/', views.playlist, name='playlist'),
    path('playlist_confirmacion/', views.playlist_confirmacion, name='playlist_confirmacion'),
]
