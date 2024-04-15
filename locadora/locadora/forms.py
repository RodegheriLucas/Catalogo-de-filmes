from django import forms
from .models import *

class FilmesForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = '__all__'