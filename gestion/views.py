from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

#from .models import *
#from django.http import JsonResponse
#import json
#import datetime
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
def enfermeros(request):

    return render(request, 'registration/enfermeros.html')

def secretario(request):

    return render(request, 'registration/secretario.html')

def salir (request):
   logout(request)
   return redirect('/')
