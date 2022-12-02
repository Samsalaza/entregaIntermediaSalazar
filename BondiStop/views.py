from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from BondiStop.forms import formularioClientes


def inicio (request):
    return render (request, "BondiStop/inicio.html")

def clientes (request):
    return render (request, "BondiStop/clientes.html")

def empleados (request):
    return render (request, "BondiStop/empleados.html")

def menues (request):
    return render (request, "BondiStop/menues.html")

def formularioClientes (request):
    return render ("BondiStop/formularioClientes.html")