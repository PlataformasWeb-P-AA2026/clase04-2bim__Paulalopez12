from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from negocio.models import Comentario, Restaurante, Chef, Plato

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_cocina', 'capacidad_meses']

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ['nombres', 'anios_experiencia', 'especialidad_culinaria',
                  'restaurante']

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio_plato',
                  'ingredientes_principales', 'chef']
        
class ComentarioForm(ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comentario
        fields = ['comentario']
        labels = {
            'comentario': _('Ingrese su comentario'),
        }

    def clean_comentario(self):
        valor = self.cleaned_data['comentario']
        if len(valor) < 25:
            raise forms.ValidationError("Ingrese un comentario de al menos 25 caracteres")
        return valor
