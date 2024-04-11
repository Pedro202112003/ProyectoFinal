from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('doctores/', views.doctores, name='doctores'),
    path('contactos/', views.contactos, name='contactos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('enfermeros/', views.enfermeros, name='enfermeros'), # la parte de entrar al analisis 
    path('secretario/', views.secretario, name='secretario'),
    path('salir/', views.salir, name='salir'),
]