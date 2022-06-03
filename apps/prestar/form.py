from django.forms import ModelForm
from .models import Prestar,Usuarios

class PrestarForm(ModelForm):
    class Meta:
        model = Prestar
        fields = '__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'