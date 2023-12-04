from django.contrib import admin

from .models import Contactos

class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'celular', )
    list_filter = ('email', )
    search_fields = ('nombre', 'apellido', 'email', 'celular', )

# Register your models here.
admin.site.register(Contactos, ContactosAdmin)
