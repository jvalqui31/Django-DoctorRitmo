from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = [
           'title',
           'description',
           'image',
           'link'
        ]
        labels = {
            'title' : 'Título',
            'description' : 'Descripción',
            'image' : 'Imagen',
            'link' : 'link'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'}),
            'link' : forms.TextInput(attrs={'class':'form-control','type':'url'})
        }