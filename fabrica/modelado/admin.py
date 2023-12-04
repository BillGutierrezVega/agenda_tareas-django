from django.contrib import admin

from .models import Salario, Poblacion, PuestoLaboral, FabricaLaboral, Empleado

class PoblacionAdmin(admin.ModelAdmin):
    list_display = ('pais', 'departamentos', )
    list_filter = ('pais', 'departamentos', )
    search_fields = ('pais', 'departamentos', )

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'puesto_laboral', 'fabrica_laboral', )
    list_filter = ('nombre', 'email', )
    search_fields = ('nombre', 'email', )

# Register your models here.
admin.site.register(Salario)
admin.site.register(Poblacion, PoblacionAdmin)
admin.site.register(PuestoLaboral)
admin.site.register(FabricaLaboral)
admin.site.register(Empleado, EmpleadoAdmin)