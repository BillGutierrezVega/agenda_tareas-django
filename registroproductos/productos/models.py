from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    imagen = models.ImageField(blank=False, null=False, upload_to='static/images')
    
    def __str__(self):
        return self.nombre