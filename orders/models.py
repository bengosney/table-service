# Django
from django.db import models
from django.utils.translation import gettext as _

# First Party
from tableservice.modelMixins import BaseModel, Info, NoDelete


class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name_plural = "Categories"


class Product(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    in_stock = models.BooleanField(_("In Stock"), default=True)
    categories = models.ManyToManyField(Category)


class Table(BaseModel):
    pass


class Order(NoDelete, Info):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
