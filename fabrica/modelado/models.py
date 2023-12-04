from django.db import models

# Create your models here.
class Salario(models.Model):
    bruto_cobrar = models.DecimalField(max_digits=10, decimal_places=2)
    pago_extra = models.BooleanField()
    
    def __str__(self):
        return str(self.bruto_cobrar)

class PuestoLaboral(models.Model):
    nombre_cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_cargo

class Poblacion(models.Model):
    pais = models.CharField(max_length=100)
    departamentos = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pais

class FabricaLaboral(models.Model):
    nombre_fabrica = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    cod_postal = models.CharField(max_length=100)
    poblacion = models.OneToOneField(Poblacion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_fabrica

class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=200)
    direccion = models.CharField(max_length=200)
    puesto_laboral = models.OneToOneField(PuestoLaboral, on_delete=models.CASCADE)
    fabrica_laboral = models.OneToOneField(FabricaLaboral, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre