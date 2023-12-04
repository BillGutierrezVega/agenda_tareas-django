from django import forms

from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = (
            'nombre', 
            'descripcion_corta', 
            'descripcion', 
            'fecha_creacion', 
            'fecha_limite'
            )
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion_corta': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'fecha_creacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_limite': forms.TextInput(attrs={'class':'form-control'})
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) > 150:
            raise forms.ValidationError('Nombre muy grande, debe tener 10 caracteres o menos.')
        return nombre