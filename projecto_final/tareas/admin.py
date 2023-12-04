from django.contrib import admin

from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta', 'fecha_creacion', 'fecha_limite', )
    list_filter = ('nombre', )
    search_fields =  ('nombre', 'descripcion_corta', )

# Register your models here.
admin.site.register(Tarea, TareaAdmin)