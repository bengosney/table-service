# Standard Library
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


SCHEMA_TYPE_FETCH = "fetch"
SCHEMA_TYPE_CREATE = "create"
SCHEMA_TYPE_UPDATE = "update"
SCHEMA_TYPES = [SCHEMA_TYPE_FETCH, SCHEMA_TYPE_CREATE, SCHEMA_TYPE_UPDATE]


def make_schemas(model: Type[Model], schema_types: List[str] = SCHEMA_TYPES, depth: int = 0) -> List[Type[Schema]]:
    schemas = []
    if SCHEMA_TYPE_FETCH in schema_types:
        schemas.append(
            create_schema(
                model, depth=depth, name=f"{model._meta.verbose_name.title()}", exclude=getattr(model, "_exclude", [])
            )
        )

    if SCHEMA_TYPE_CREATE in schema_types:
        schemas.append(
            create_schema(
                model, name=f"{model._meta.verbose_name.title()} Create", exclude=getattr(model, "_exclude_create", [])
            )
        )

    if SCHEMA_TYPE_UPDATE in schema_types:
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
