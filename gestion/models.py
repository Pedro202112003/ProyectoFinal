from django.db import models

#from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    apellido=models.CharField(max_length=30, null=False)
    email=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=8, null=True)
    tipo=models.CharField(max_length=15 , null=False) #tipo de anailis
    realizado = models.BooleanField(default=False, null=True, blank=True)
    imagen  = models.ImageField(null=True, blank=True)
   # cui=models.FloatField(null=False)
   # nacimineto = models.DateTimeField(blank=False)
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url
   # imagen=models.ImageField(null=True, blank=True)
    def _str_(self):
        return self.nombre

class Analisis(models.Model):
    paciente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.paciente



