# Standard Library
from enum import Enum, unique
from typing import List, Type

# Django
from django.db.models import Model

# Third Party
from ninja.orm import create_schema
from ninja.schema import Schema


def make_all_optional(schema: Type[Schema]) -> Type[Schema]:
    for key in schema.__fields__:
        schema.__fields__.get(key).required = False

    return schema


@unique
class schema_types(Enum):
    FETCH = 1
    CREATE = 2
    UPDATE = 3


def make_schemas(
    model: Type[Model], types: List[schema_types] = list(schema_types), depth: int = 0
) -> List[Type[Schema]]:
    schemas = []
    if schema_types.FETCH in types:
        schemas.append(
            create_schema(
                model, depth=depth, name=f"{model._meta.verbose_name.title()}", exclude=getattr(model, "_exclude", [])
            )
        )

    if schema_types.CREATE in types:
        schemas.append(
            create_schema(
                model, name=f"{model._meta.verbose_name.title()} Create", exclude=getattr(model, "_exclude_create", [])
            )
        )

    if schema_types.UPDATE in types:
        schemas.append(
            make_all_optional(
                create_schema(
                    model,
                    name=f"{model._meta.verbose_name.title()} Update",
                    exclude=getattr(model, "_exclude_create", []),
                )
            )
        )

    return schemas
