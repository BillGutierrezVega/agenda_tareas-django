from django import forms

from .models import Contactos


class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('nombre', 'apellido', 'email', 'celular', 'direccion', 'fecha_creacion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_creacion': forms.TextInput(attrs={'class':'form-control'})
        }
        

class FormularioMulti(forms.Form):
    nombre = forms.CharField(max_length=150)