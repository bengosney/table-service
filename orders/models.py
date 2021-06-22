# Standard Library
from enum import Enum, auto

# Django
from django.db import models
from django.utils.translation import gettext as _

# Third Party
from django_fsm import FSMField, transition

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
    price = models.FloatField(_("Price"), default=0)


class Table(BaseModel):
    pass


class OrderStates(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    Unprocessed = auto()
    Processing = auto()
    Processed = auto()

    @classmethod
    def choices(cls):
        return [[name, name] for name, _ in cls.__members__.items()]

    @classmethod
    def maxLength(cls):
        return max(len(item.value) for _, item in cls.__members__.items())


class Order(NoDelete, Info):

    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)

    state = FSMField(
        _("State"),
        default=OrderStates.Unprocessed,
        choices=OrderStates.choices(),
        protected=True,
        max_length=OrderStates.maxLength(),
    )

    @transition(field=state, source=OrderStates.Unprocessed, target=OrderStates.Processing)
    def processing(self):
        pass

    @transition(field=state, source=[OrderStates.Unprocessed, OrderStates.Processing], target=OrderStates.Processed)
    def processed(self):
        pass
