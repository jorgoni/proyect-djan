from django import forms
from .models import Arbol
from .models import Tarea

class ArbolForm(forms.Form):
    pregunta = forms.CharField(max_length=100)
    respuesta= forms.CharField(max_length=100)

class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['tarea']