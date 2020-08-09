"""Pro_Factura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Factura.views import menu,listarCliente,cliente,editarCliente,eliminarCliente,listarFactura,listarProducto,producto,editarProducto,eliminarProducto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='index'),
    path('listarcliente/', listarCliente, name='listarcliente'),
    path('cliente/', cliente, name='cliente'),
    path('editarcliente/<int:id>/', editarCliente, name='editarcliente'),
    path('eliminarcliente/<int:id>', eliminarCliente, name='eliminarcliente'),
    path('listarfactura/', listarFactura, name='listarfactura'),
    path('listarproducto/', listarProducto, name='listarproducto'),
    path('producto/', producto, name='producto'),
    path('editarproducto/<int:id>/', editarProducto, name='editarproducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarproducto'),
]
