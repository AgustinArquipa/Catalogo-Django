from django import forms
from catalogo.models import Genero, Autor
from django.forms.widgets import NumberInput

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ('nombre',)

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('apellido', 'nombre', 'fechaNac', 'fechaDeceso', 'foto')

        widgets = {
            'fechaNac':NumberInput(attrs={'type':'date'}),
            'fechaDeceso':NumberInput(attrs={'type':'date'}),
        }