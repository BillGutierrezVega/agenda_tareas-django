from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'stok',)
    search_fields = ('name', 'short_description',)
    list_filter = ('stok', 'ultimo_descuento', )
    date_hierarchy = 'ultimo_descuento'
    
# Register your models here.
admin.site.register(Product, ProductAdmin)