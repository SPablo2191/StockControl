from django.contrib import admin
from .models import Product, Supplier


# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "DNI")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "current_stock")


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin) 