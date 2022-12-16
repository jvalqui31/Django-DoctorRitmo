from django import forms
from django.forms import ModelForm
from .models import Curso

class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = [
           'idCurso',
           'descripcion',
           'precio',
           'stock',
           'imagen',
           'docente'
        ]
        labels = {
            'idCurso' : 'Código Curso',
            'descripcion' : 'Descripción',
            'precio' : 'Precio',
            'stock' : 'Stock',
            'imagen' : 'Imagen',
            'docente' : 'Profesor'
        }
        widgets = {
            'idCurso' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock' :  forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'}),
            'docente' : forms.Select(attrs={'class':'form-control'})
        }