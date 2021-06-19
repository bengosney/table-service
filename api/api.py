# Standard Library
from typing import List, Type

# Django
from django.db.models import Model
from django.shortcuts import get_object_or_404

# Third Party
from ninja import Router
from ninja.schema import Schema

# First Party
from tableservice.auth import AuthBearer


def ucfirst(string: str) -> str:
    return string[0].upper() + string[1:]


def make_CRUD(
    model: Type[Model], responseSchema: Type[Schema], createSchema: Type[Schema], updateSchema: Type[Schema]
) -> Router:
    router = Router()

    nameSingular = model._meta.verbose_name.title()
    namePlural = model._meta.verbose_name_plural.title()

    @router.get("/", response=List[responseSchema], summary=f"List {namePlural}", description=f"List {namePlural}")
    def list(request) -> List[model]:
        return [i for i in model.objects.all()]

    @router.get(
        "/{id}",
        response=responseSchema,
        summary=ucfirst(f"{namePlural} details"),
        description=f"Get {nameSingular} details",
    )
    def details(request, id: int) -> model:
        return get_object_or_404(model, id=id)

    @router.post(
        "/",
        response=responseSchema,
        auth=AuthBearer(),
        summary=f"Create {nameSingular}",
        description=f"Create a new {nameSingular}",
    )
    def create(request, payload: createSchema):
        return model.objects.create(**payload.dict())

    @router.put(
        "/{id}", response=responseSchema, summary=f"Update {nameSingular}", description=f"Update a {nameSingular}"
    )
    def update(request, payload: updateSchema, id: int):
        item = get_object_or_404(model, id=id)

        for attr, value in payload.dict().items():
            setattr(item, attr, value)

        item.save()

        return item

    @router.delete("/{id}", summary=f"Delete {nameSingular}", description=f"Delete a {nameSingular}")
    def delete(request, id: int):
        item = get_object_or_404(model, id=id)
        item.delete()

        return {"success": True}

    return router
