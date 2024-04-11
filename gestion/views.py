from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

# Create your views here.

from .models import *
from django.http import JsonResponse
import json
import datetime
#from .utils import *

# Create your views here.
def inicio(request):

    return render(request, 'apartados/inicio.html')

def nosotros(request):

    return render(request, 'apartados/nosotros.html')

def servicios(request):

    return render(request, 'apartados/servicios.html')

def doctores(request):

    return render(request, 'apartados/doctores.html')

def contactos(request):

    return render(request, 'apartados/contactos.html')

@login_required
def menu(request):
    
    return render(request, 'programa/menu.html')

@login_required
@csrf_protect
def ingreso(request):
    if request.method == 'POST':
        nombreIngresadoForm = request.POST.get('nombre')
        apellidoIngresadoForm = request.POST.get('apellido')
        emailIngresadoForm = request.POST.get('email')
        telefonoIngresadoForm = request.POST.get('telefono')
        tipoIngresadoForm = request.POST.get('tipo')
        # Obtén el resto de los datos del formulario de la misma manera
        
        # Crear una instancia de tu modelo con los datos recibidos
        guardar = Cliente(nombre=nombreIngresadoForm, apellido = apellidoIngresadoForm, email=emailIngresadoForm, telefono = telefonoIngresadoForm, tipo=tipoIngresadoForm)
        guardar.save()  # Guardar la instancia en la base de datos
        messages.success(request, 'El ingreso se realizó correctamente.')
    return render(request, 'programa/ingreso.html')

@login_required
def analisis(request):

    return render(request, 'programa/analisis.html')

@login_required
def resultados(request):

    return render(request, 'programa/resultados.html')

def salir (request):
    logout(request)
    return redirect('/')