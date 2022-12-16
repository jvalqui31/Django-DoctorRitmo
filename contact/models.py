from django.db import models

# Create your models here.

class Contacto(models.Model):
    name = models.CharField(max_length=15)
    rut = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=15)
    genero = models.CharField(max_length=10)
    instrumento = models.CharField(max_length=10)
    comuna = models.CharField(max_length=15)
    comentarios = models.CharField(max_length=200)
    def __str__(self):
        return self.rut