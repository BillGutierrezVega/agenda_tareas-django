from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name
    

class Restaurant(models.Model):
    number_of_employees = models.IntegerField(default=1)
    place = models.OneToOneField("Place", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.place.name
