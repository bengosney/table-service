# Standard Library
from enum import Enum, unique
from typing import List, Type, Union

# Django
from django.db.models import Model

# Third Party
from ninja.orm import create_schema
from ninja.schema import Schema

# First Party
from api.utils import verbose_name


def make_all_optional(schema: Type[Schema]) -> Type[Schema]:
    for key in schema.__fields__:
        field = schema.__fields__.get(key)
        if field is not None:
            field.required = False

    return schema


@unique
class schema_types(Enum):
    FETCH = 0
    CREATE = 1
    UPDATE = 2


def make_schemas(
    model: Type[Model], types: List[schema_types] = list(schema_types), depth: int = 0
) -> List[Union[None, Type[Schema]]]:
    schemas: List[Union[None, Type[Schema]]] = [None for _ in schema_types]

    valid_fields = [f.name for f in model._meta.get_fields()]
    try:
        exclude = [f for f in model._exclude if f in valid_fields]  # type: ignore
    except AttributeError:
        exclude = []

    try:
        create_exclude = [f for f in model._exclude_create if f in valid_fields]  # type: ignore
    except AttributeError:
        create_exclude = []

    if schema_types.FETCH in types:
        schemas[schema_types.FETCH.value] = create_schema(model, depth=depth, name=verbose_name(model), exclude=exclude)

    if schema_types.CREATE in types:
        schemas[schema_types.CREATE.value] = create_schema(
            model, name=f"{verbose_name(model)} Create", exclude=create_exclude
        )

    if schema_types.UPDATE in types:
        schemas[schema_types.UPDATE.value] = make_all_optional(
            create_schema(
                model,
                name=f"{verbose_name(model)} Update",
                exclude=create_exclude,
            )
        )

    return schemas
