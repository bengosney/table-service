# Django
from django.db import models
from django.utils.translation import gettext as _


class BaseMixin:
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, editable=False)
    deleted = models.BooleanField(_("Deleted"), default=False)

    class Meta:
        abstract = True
        ordering = ("positon", "-created")


class Product(models.Model, BaseMixin):
    title = models.CharField(_("Name"), max_length=255)
    in_stock = models.BooleanField(_("In Stock"), default=True)


class Table(models.Model, BaseMixin):
    pass


class Order(models.Model, BaseMixin):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
