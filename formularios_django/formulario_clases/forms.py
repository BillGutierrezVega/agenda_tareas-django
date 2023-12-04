from django import forms

class CommentsForm(forms.Form):
    name = forms.CharField(label='Ingrese su nombre', max_length=100, help_text='100 caracteres máximo')
    url = forms.URLField(label="Ingrese su url", required=False, initial='http://')
    comment = forms.CharField(label='Ingrese su comentario', max_length=100)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name[0].isupper():
            raise forms.ValidationError('El nombre debe de comenzar con mayúsula')
        return name


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label='Ingresa tu nombre ',
        widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(
        label='Ingresa tu email ', 
        max_length=50,
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField(
        label='Ingrese su mensaje ',
        widget=forms.TextInput(attrs={'class':'form-control'}))


class Profesor(forms.Form):
    nombre = forms.CharField(label='Ingresa tu nombre', max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(label='Ingresa tu apellido', max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
    curso = forms.CharField(label='Ingresa el curso', max_length=60, widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.IntegerField(label='Ingresa tu edad', max_value=80, widget=forms.NumberInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Ingrese su email', max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre != 'Bill':
            raise forms.ValidationError('Solo se permite Bill')
        else:
            return nombre
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@casa.com'):
            raise forms.ValidationError('Solo se permite email de casa')
        return email
    
    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad <= 18:
            raise forms.ValidationError('Solo se admiten mayores de edad')
        return edad
    
    def clean_curso(self):
        curso = self.cleaned_data.get('curso')
        cursos = ['historia', 'lenguaje', 'matematicas']
        if curso not in cursos:
            raise forms.ValidationError('Escoje un curso válido')
        return curso
    
    
class AlumnosForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(label='Edad', widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre or not nombre[0].isupper():
            raise forms.ValidationError('Nombre inicia con mayúscula')
        return nombre