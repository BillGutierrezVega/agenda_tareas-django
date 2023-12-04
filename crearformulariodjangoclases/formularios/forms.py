from django import forms 

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(label='Ingrese su nombre', required=False, widget=forms.TextInput(attrs={'class':'input_nombre'}))
    apellido = forms.CharField(label='Ingrese su apellido', widget=forms.TextInput(attrs={'class':'input_apellido'}))
    edad = forms.IntegerField(label='Ingresa tu edad', widget=forms.NumberInput(attrs={'class':'input_edad'}))
    dni = forms.CharField(label='Ingresa tu dni', widget=forms.TextInput(attrs={'class':'input_dni'}))