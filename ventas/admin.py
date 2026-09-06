from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Cliente, TelefonoCliente, Venta, DetalleVenta

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(TelefonoCliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)