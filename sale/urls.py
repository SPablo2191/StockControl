from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/products", views.get_products, name="products"),
    path("/product", views.add_product, name="add_product"),
    path("/register_product", views.register_product, name="register_product"),
]
