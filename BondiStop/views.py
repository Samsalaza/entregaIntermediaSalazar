from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from BondiStop.forms import clientesForm


def inicio (request):
    return render (request, "BondiStop/inicio.html")

def clientes (request):
    return render (request, "BondiStop/clientes.html")

def empleados (request):
    return render (request, "BondiStop/empleados.html")

def menues (request):
    return render (request, "BondiStop/menues.html")

def formularioClientes (request):

    if request.method=="POST":
        form=clientesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            telefono=info["telefono"]
            regular=info["regular"]

            cliente_Form=Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono, regular=regular)
            cliente_Form.save()
            return render (request, "BondiStop/inicio.html")

    else:
        formulario=clientesForm

    return render (request, "BondiStop/formularioClientes.html", {"form": formulario})


def busquedaEmpleado (request):
        return render(request, "BondiStop/buscarEmpleado.html")


def buscar (request):

    if request.GET["dni"]:
        dni=request.GET["dni"]
        empleado=Empleado.objects.filter(dni__icontains=dni)
        return render(request, "BondiStop/resultadoBusqueda.html",{"empleado":empleado})
    else:
        return render (request, "BondiStop/buscarEmpleado.html",{"mensaje":"INGRESA UN DNI VALIDO DE EMPLEADO"})