from django.db import models
from ..libro.models import Libro

# Create your models here.
class Ejemplares(models.Model):
    localizacion = models.CharField(max_length=250)
    codigo_libro = models.ForeignKey(Libro,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.localizacion
        
