from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.


#class clientesadmin(admin.ModelAdmin):
   # list_display=("nombre", "apellido", "email", "telefono", "tipo")
    #search_fields=("usuario", "nombre", "direccion", "email", "telefono")

#class analisisadmin(admin.ModelAdmin):
    #list_filter= ("seccion")
   # list_display=("paciente", "fecha", "analisis", "resultado")
    #search_fields=("nombre", "seccion", "precio")
    


admin.site.register(Cliente)
admin.site.register(Analisis)
