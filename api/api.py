# Standard Library
from enum import Enum, unique
from typing import Any, List, Type

# Django
from django.db.models import Model
from django.shortcuts import get_object_or_404

# Third Party
from ninja import Router
from ninja.constants import NOT_SET

# First Party
from api.schema import make_schemas


def ucfirst(string: str) -> str:
    return string[0].upper() + string[1:]


@unique
class CRUD_types(Enum):
    LIST = 1
    DETAILS = 2
    CREATE = 3
    UPDATE = 4
    DELETE = 5


def make_CRUD(
    model: Type[Model], read_auth: Any = NOT_SET, write_auth: Any = NOT_SET, types: List[CRUD_types] = list(CRUD_types)
) -> Router:
    router = Router()

    responseSchema, createSchema, updateSchema = make_schemas(model)

    nameSingular = model._meta.verbose_name.title()
    namePlural = model._meta.verbose_name_plural.title()

    id = f"{model._meta.app_label}-{model._meta.model_name}"

    if CRUD_types.LIST in types:

        @router.get(
            "/",
            response=List[responseSchema],
            operation_id=f"{id}-list",
            summary=f"List {namePlural}",
            auth=read_auth,
            description=f"List {namePlural}",
        )
        def list(request) -> List[model]:
            return [i for i in model.objects.all()]

    if CRUD_types.DETAILS in types:

        @router.get(
            "/{id}",
            response=responseSchema,
            auth=read_auth,
            operation_id=f"{id}-details",
            summary=ucfirst(f"{namePlural} details"),
            description=f"Get {nameSingular} details",
        )
        def details(request, id: int) -> model:
            return get_object_or_404(model, id=id)

    if CRUD_types.CREATE in types:

        @router.post(
            "/",
            response=responseSchema,
            auth=write_auth,
            operation_id=f"{id}-create",
            summary=f"Create {nameSingular}",
            description=f"Create a new {nameSingular}",
        )
        def create(request, payload: createSchema):
            return model.objects.create(**payload.dict())

    if CRUD_types.UPDATE in types:

        @router.put(
            "/{id}",
            response=responseSchema,
            auth=write_auth,
            operation_id=f"{id}-update",
            summary=f"Update {nameSingular}",
            description=f"Update a {nameSingular}",
        )
        def update(request, payload: updateSchema, id: int):
            item = get_object_or_404(model, id=id)

            for attr, value in payload.dict().items():
                setattr(item, attr, value)

            item.save()

            return item

    if CRUD_types.DELETE in types:

        @router.delete(
            "/{id}",
            auth=write_auth,
            operation_id=f"{id}-delete",
            summary=f"Delete {nameSingular}",
            description=f"Delete a {nameSingular}",
        )
        def delete(request, id: int):
            item = get_object_or_404(model, id=id)
            item.delete()

            return {"success": True}

    return router
