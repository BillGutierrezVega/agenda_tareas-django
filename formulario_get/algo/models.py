from django.db import models

class Personabien(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    
    def __str__(self):
        return self.nombre
