from django import forms

class clientesForm (forms.Form):
    nombre=forms.CharField( max_length=50)
    apellido=forms.CharField( max_length=50)
    email=forms.EmailField( max_length=254)
    telefono=forms.IntegerField()
    regular=forms.BooleanField()