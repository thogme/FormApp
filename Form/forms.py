from django import forms
from .models import List

class Formulario(forms.ModelForm):

    class Meta:
        model = List
        fields = ('nombre', 'numero')
