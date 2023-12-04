from django.db import models
from datetime import date

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(default=date.today)
    fecha_limite = models.DateField()
    
    def __str__(self):
        return self.nombre