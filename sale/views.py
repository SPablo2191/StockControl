from django.shortcuts import get_object_or_404, render
from django.http import request, HttpResponse
from .models import Product, Supplier
from django.template import RequestContext, loader



# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_products(request):
    products = Product.objects.order_by("id")
    template = loader.get_template("products.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))

def get_suppliers(request):
    suppliers = Supplier.objects.order_by("id")
    template = loader.get_template("suppliers.html")
    context = {
        "suppliers": suppliers,
    }
    return HttpResponse(template.render(context, request))


def add_product(request):
    suppliers = Supplier.objects.order_by("id")
    template = loader.get_template("add_product.html")
    context = {
        "suppliers": suppliers,
    }
    return HttpResponse(template.render(context, request))


def add_supplier(request):
    return render(request, 'add_supplier.html')


def register_product(request):
    try:
        supplier_id = request.POST.get("supplier", False)
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        name = request.POST.get("name", False)
        price = request.POST.get("price", False)
        current_stock = request.POST.get("current_stock", False)
    except:
        return HttpResponse("Error no se pudo completar el formulario.")
    finally:
        new_product = Product(
            name=name, price=price, current_stock=current_stock, supplier=supplier
        )
        new_product.save()
    template = loader.get_template("success.html")
    context = {
        "message": "Se registro el producto con exito!!!",
    }
    return HttpResponse(template.render(context, request))


def register_supplier(request):
    try:
        name = request.POST.get("name", False)
        last_name = request.POST.get("last_name", False)
        DNI = request.POST.get("DNI", False)
    except:
        return HttpResponse("Error no se pudo completar el formulario.")
    finally:
        new_supplier = Supplier(name=name, last_name=last_name, DNI=DNI)
        new_supplier.save()
    template = loader.get_template("success.html")
    context = {
        "message": "Se registro el proveedor con exito!!!",
    }
    return HttpResponse(template.render(context, request))
