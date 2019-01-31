from django.contrib import admin
from .models import Categoria,Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ["nombre","slug"]
    prepopulated_fields = { "slug" : ('nombre',)}


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","slug","precio","almacen","disponibilidad","creado","actualizado"]
    list_filter =['disponibilidad','actualizado','creado']
    list_editable=['precio','disponibilidad']
    prepopulated_fields = { "slug" : ('nombre',)}



