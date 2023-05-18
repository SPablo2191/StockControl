from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Product
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def get_products(request):
    products = Product.objects.order_by("name")
    template = loader.get_template("products.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))

def add_product(request):
    template = loader.get_template("add_product.html")
    return HttpResponse(template.render())
