from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("products", views.get_products, name="products"),
    path("product", views.add_product, name="add_product"),
]
