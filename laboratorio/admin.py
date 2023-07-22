from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
from laboratorio.models import Laboratorio, DirectorGeneral, Producto


# Register your models here.

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio", "year", "p_costo", "p_venta" )

    def year(self, obj):
        return obj.f_fabricacion.strftime("%Y")
    





