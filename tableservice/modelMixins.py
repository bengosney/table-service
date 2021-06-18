# Django
from django.db import models
from django.utils.translation import gettext as _


class BaseMixin(models.Model):
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, editable=False)
    deleted = models.BooleanField(_("Deleted"), default=False)

    _exclude = ["deleted"]
    _exclude_create = ["position", "created", "last_updated", "deleted"]

    class Meta:
        abstract = True
        ordering = ("position", "-created")
