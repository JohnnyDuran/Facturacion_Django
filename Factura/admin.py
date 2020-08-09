from django.contrib import admin
from .models import Producto,Cliente,Factura,DetalleFactura
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('descripcion','precio','stock','iva','creacion')
    ordering = ('descripcion', )
    search_fields = ('descripcion', )
    list_filter = ('descripcion', )

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('ruc','nombre','direccion','creacion')
    ordering = ('nombre', )
    search_fields = ('nombre','direccion', )
    list_filter = ('nombre', )

class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('cliente','fecha','total','creacion')
    ordering = ('fecha',)
    search_fields = ('cliente','fecha',)
    list_filter = ('cliente',)



admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)

#Para ingresar como administrador
#usuario: johnny
#password: johnny