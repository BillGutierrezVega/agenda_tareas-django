from django.db import models
from datetime import date

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    celular = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    fecha_creacion = models.DateField(default=date.today)
    
    def __str__(self):
        return self.nombre
    