from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    short_description = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    stok = models.IntegerField(default=20)
    ultimo_descuento = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name