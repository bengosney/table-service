# Django
from django.db import models
from django.utils.translation import gettext as _

# First Party
from tableservice.modelMixins import BaseMixin


class Product(BaseMixin):
    name = models.CharField(_("Name"), max_length=255)
    in_stock = models.BooleanField(_("In Stock"), default=True)
