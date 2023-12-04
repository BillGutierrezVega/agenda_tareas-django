from django.forms import ModelForm, TextInput, EmailInput

from .models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }
        fields = ['name', 'last_name', 'email']