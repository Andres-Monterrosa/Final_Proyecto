from django.db import models
from django.utils import timezone
from ..ejemplares.models import Ejemplares


class Usuarios(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.nombre

class Prestar(models.Model):
    fecha_dev = models.DateField(default=timezone.now)
    fecha_pres = models.DateField(default=timezone.now)
    ejemplares = models.ForeignKey(Ejemplares,on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuarios,on_delete=models.CASCADE)


