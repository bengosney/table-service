# Django
from django.db import models

# First Party
from products.models import Product
from tables.models import Table
from tableservice.modelMixins import Info, NoDelete


class Order(NoDelete, Info):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
