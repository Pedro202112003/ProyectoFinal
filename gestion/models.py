from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    cui=models.FloatField(null=False)
    nacimineto = models.DateTimeField(blank=False)
    correo=models.EmailField(null=True, blank=True)
    imagen=models.ImageField(null=True, blank=True)
    def _str_(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url


