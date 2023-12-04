from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name


class Comentarios(models.Model):
    comenta = models.CharField(max_length=100)
    ratings = models.IntegerField(default=3)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comenta