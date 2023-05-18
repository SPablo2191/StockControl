from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Product
from django.template import loader
# Create your views here.
def get_products(request):
    products = Product.objects.order_by('name')
    template = loader.get_template("index.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))