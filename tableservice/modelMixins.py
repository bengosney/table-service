# Standard Library
from typing import Any, Dict, Tuple

# Django
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext as _


class NoDelete(models.Model):
    class Meta:
        abstract = True

    def delete(self, using: Any, keep_parents: bool) -> Tuple[int, Dict[str, int]]:
        return (0, {})


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super().update(deleted=True)

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(deleted=None)

    def dead(self):
        return self.exclude(deleted=None)


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return SoftDeletionQuerySet(self.model).filter(deleted=None)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDelete(models.Model):
    deleted = models.BooleanField(_("Deleted"), default=False)

    objects = SoftDeletionManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using: Any, keep_parents: bool) -> Tuple[int, Dict[str, int]]:
        self.deleted = True
        self.save()

        return (1, {f"{self.__class__}": 1})

    def hard_delete(self, using: Any, keep_parents: bool) -> Tuple[int, Dict[str, int]]:
        return super().delete(using=using, keep_parents=keep_parents)


class Info(models.Model):
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, editable=False)

    _exclude = []
    _exclude_create = [
        "id",
        "position",
        "created",
        "last_updated",
        "deleted",
    ]

    class Meta:
        abstract = True
        ordering = ("position", "-created")

    def __str__(self) -> str:
        return getattr(self, "name", super().__str__())


class BaseModel(SoftDelete, Info):
    class Meta(SoftDelete.Meta, Info.Meta):
        abstract = True
