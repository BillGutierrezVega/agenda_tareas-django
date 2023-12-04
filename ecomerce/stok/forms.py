from django import forms
from django.forms import ModelForm

from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'short_description', 'description', 'stok')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'})
        }