from django.shortcuts import render
from django.http import HttpResponse

from .models import Place, Restaurant

# Create your views here.
def create(_request):
    # Place.objects.create(name='casa-restaurant', address="calle random")
    place = Place(name="casa2", address="calle random2")
    place.save()
    
    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)