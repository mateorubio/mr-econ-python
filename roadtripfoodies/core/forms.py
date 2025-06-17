from django import forms
from .models import Receta, Autor, Destino

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'