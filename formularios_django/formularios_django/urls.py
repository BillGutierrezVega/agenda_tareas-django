
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario_clases/', include('formulario_clases.urls'))
]
