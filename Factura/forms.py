from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion')
        label = {'ruc': 'Ruc', 'nombre': 'Nombre', 'Direccion': 'Dirección'}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripción', 'precio': 'Precio', 'stock': 'Stock de Productos', 'iva': 'IVA'}