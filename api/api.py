# Standard Library
from enum import Enum, unique
from typing import Any, Dict, List, Type

# Django
from django.db.models import Model
from django.shortcuts import get_object_or_404

# Third Party
from ninja import Router
from ninja.constants import NOT_SET

# First Party
from api.schema import make_schemas, schema_types
from api.utils import verbose_name, verbose_name_plural


def ucfirst(string: str) -> str:
    return string[0].upper() + string[1:]


@unique
class CRUD_types(Enum):
    LIST = 0
    DETAILS = 1
    CREATE = 2
    UPDATE = 3
    DELETE = 4

    @classmethod
    def get_type_map(cls) -> Dict["CRUD_types", List[schema_types]]:
        return {
            cls.LIST: [schema_types.FETCH],
            cls.DETAILS: [schema_types.FETCH],
            cls.CREATE: [schema_types.CREATE, schema_types.CREATE],
            cls.UPDATE: [schema_types.UPDATE, schema_types.CREATE],
            cls.DELETE: [],
        }

    @classmethod
    def get(cls, exclude: List["CRUD_types"] = []) -> List["CRUD_types"]:
        return [t for t in cls if t not in exclude]


def make_CRUD(
    model: Type[Model], read_auth: Any = NOT_SET, write_auth: Any = NOT_SET, types: List[CRUD_types] = list(CRUD_types)
) -> Router:
    router = Router()

    required_schemas = [i for t in types for i in CRUD_types.get_type_map()[t]]
    responseSchema, createSchema, updateSchema = make_schemas(model, types=required_schemas)

    nameSingular = verbose_name(model)
    namePlural = verbose_name_plural(model)

    id = f"{model._meta.app_label}-{model._meta.model_name}"

    if CRUD_types.LIST in types and responseSchema is not None:

        @router.get(
            "/list",
            response=List[responseSchema],  # type: ignore
            operation_id=f"{id}-list",
            summary=f"List {namePlural}",
            auth=read_auth,
            description=f"List {namePlural}",
        )
        def list(request) -> List[Type[Model]]:
            return [i for i in model.objects.all()]

    if CRUD_types.DETAILS in types and responseSchema is not None:

        @router.get(
            "/{id}",
            response=responseSchema,
            auth=read_auth,
            operation_id=f"{id}-details",
            summary=ucfirst(f"{namePlural} details"),
            description=f"Get {nameSingular} details",
        )
        def details(request, id: int) -> Model:
            return get_object_or_404(model, id=id)

    if CRUD_types.CREATE in types and createSchema is not None:

        @router.post(
            "/",
            response=responseSchema,
            auth=write_auth,
            operation_id=f"{id}-create",
            summary=f"Create {nameSingular}",
            description=f"Create a new {nameSingular}",
        )
        def create(request, payload: createSchema):  # type: ignore
            return model.objects.create(**payload.dict())  # type: ignore

    if CRUD_types.UPDATE in types and updateSchema is not None:

        @router.put(
            "/{id}",
            response=responseSchema,
            auth=write_auth,
            operation_id=f"{id}-update",
            summary=f"Update {nameSingular}",
            description=f"Update a {nameSingular}",
        )
        def update(request, payload: updateSchema, id: int):  # type: ignore
            item = get_object_or_404(model, id=id)

            for attr, value in payload.dict().items():  # type: ignore
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
