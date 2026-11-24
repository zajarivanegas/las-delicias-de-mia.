from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "is_active", "orden")
    list_editable = ("is_active", "orden")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "is_active", "is_agotado")
    list_filter = ("categoria", "is_active", "is_agotado")