from django import forms
from locadora.models import *

class GenerosForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = '__all__'