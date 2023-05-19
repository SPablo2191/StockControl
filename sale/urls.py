from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/products", views.get_products, name="products"),
    path("/suppliers", views.get_suppliers, name="suppliers"),
    path("/product", views.add_product, name="add_product"),
    path("/supplier", views.add_supplier, name="add_supplier"),
    path("/register_product", views.register_product, name="register_product"),
    path("/register_supplier", views.register_supplier, name="register_supplier"),
]
