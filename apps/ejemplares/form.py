from django.forms import ModelForm
from .models import Ejemplares

class EjemplarForm(ModelForm):
    class Meta:
        model = Ejemplares
        fields = '__all__'