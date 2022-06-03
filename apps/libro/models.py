from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    num_pagine = models.CharField(max_length=250)
    editorial = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)
    

    def __str__(self) -> str:
        return self.titulo