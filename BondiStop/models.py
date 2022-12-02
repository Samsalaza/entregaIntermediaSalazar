from django.db import models

class Cliente (models.Model):
    nombre=models.CharField( max_length=50)
    apellido=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    telefono=models.IntegerField()
    regular=models.BooleanField()

    def __str__(self):
        return self.nombre+ " "+self.apellido

class Empleado (models.Model):
    nombre=models.CharField( max_length=50)
    apellido=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    telefono=models.IntegerField()
    dni=models.IntegerField()
    direccion=models.CharField(max_length=254)

    def __str__(self):
        return self.nombre+ " "+self.apellido

class Menues (models.Model):
    plato=models.CharField( max_length=50)
    categoria=models.CharField( max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return self.plato+ " "+self.categoria
 