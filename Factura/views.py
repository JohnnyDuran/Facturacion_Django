from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente,Factura,Producto
from .forms import ClienteForm, ProductoForm
# Create your views here.

#Vista Principal de Menu
def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración'}

    return render(request, 'principal.html', opciones)

#Vista de Listado de Clientes
def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'clientes': cliente}
    return render(request, 'listar_cliente.html', opciones)

#vista de nuevo cliente
def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'Accion': 'Crear'}
    # return HttpResponse('Cliente')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)   

#Edicion de cliente
def editarCliente(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'Accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')

    return render(request, 'cliente.html', opciones)

#Eliminacion de cliente
def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarcliente')
    return render(request, 'eliminar_cliente.html', {'Cliente': cliente})

#Vista de Registro de Ventas
def listarFactura(request):
    factura = Factura.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'facturas': factura}
    return render(request, 'listar_factura.html', opciones)

#-------------------------
# PRODUCTO
#-------------------------

#Vista de Listado de Productos
def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'productos': producto}
    return render(request, 'listar_producto.html', opciones)

#vista de nuevo producto
def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'Accion': 'Crear'}
    # return HttpResponse('Producto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)  

#Edicion de producto
def editarProducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Ventas': 'Registros de Ventas',
                'Producto': 'Productos del Blog',
                'Cliente': 'Clientes del Blog',
                'Administracion': 'Centro de Administración',
                'Accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'producto.html', opciones)

#Eliminacion de productos
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarproducto')
    return render(request, 'eliminar_producto.html', {'Producto': producto})