from django.db import models
from datetime import date

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.email
    

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(default=date.today)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline