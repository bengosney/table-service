# Standard Library
from typing import Type

# Django
from django.db import models


def verbose_name(model: Type[models.Model]):
    return model._meta.verbose_name.title() if model._meta.verbose_name is not None else f"{model.__class__}"


def verbose_name_plural(model: Type[models.Model]):
    model._meta.verbose_name_plural.title() if model._meta.verbose_name_plural is not None else f"{model.__class__}s"
