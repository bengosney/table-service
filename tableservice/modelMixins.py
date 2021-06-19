# Standard Library
from typing import Any, Dict, Tuple

# Django
from django.db import models
from django.utils.translation import gettext as _


class BaseMixin(models.Model):
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, editable=False)
    deleted = models.BooleanField(_("Deleted"), default=False)

    _exclude = []
    _exclude_create = ["id", "position", "created", "last_updated", "deleted"]

    class Meta:
        abstract = True
        ordering = ("position", "-created")

    def __str__(self) -> str:
        return getattr(self, "name", super().__str__())

    def delete(self, using: Any, keep_parents: bool) -> Tuple[int, Dict[str, int]]:
        assert self.pk is not None, "{} object can't be deleted because its {} attribute is set to None.".format(
            self._meta.object_name,
            self._meta.pk.attname,
        )
        self.deleted = True
        self.save()
        return (1, {f"{self.__class__}": 1})
