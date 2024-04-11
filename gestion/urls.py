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
    path('menu/', views.menu, name="menu"),
    path('analisis/', views.analisis, name="analisis"),
    path('ingreso/', views.ingreso, name="ingreso"),
    path('resultados/', views.resultados, name="resultados"),
    path('salir/', views.salir, name="salir"),
]