from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(max_length=1000)
    public_fecha = models.DateTimeField(default=date.today)
    rating = models.IntegerField(default=5)
    
    def __str__(self):
        return self.headline
