from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombre
    
class Canciones(models.Model):
    nombre = models.CharField(max_length=100)
    letras = models.TextField()
    
    def __str__(self):
        return self.nombre

class Playlist(models.Model):
    nombre = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cancion = models.ManyToManyField(Canciones)
    
    def __str__(self):
        return self.nombre