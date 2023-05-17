from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    DNI = models.CharField(max_length=8)


class Product(models.Model):
    name = models.TextField(max_length=255)
    price = models.FloatField()
    current_stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
