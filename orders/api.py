# Django
from django.db import transaction
from django.shortcuts import get_object_or_404

# Third Party
from django_fsm import TransitionNotAllowed
from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

# First Party
from api.api import CRUD_types, make_CRUD
from api.schema import make_schemas, schema_types
from orders.models import Category, Order, Product, Table
from tableservice.auth import AuthBearer

product_router = make_CRUD(Product, write_auth=AuthBearer)
category_router = make_CRUD(Category, write_auth=AuthBearer)
table_router = make_CRUD(Table, write_auth=AuthBearer)

product_router.add_router("/category/", category_router)

make_schemas(Order, depth=2, types=[schema_types.FETCH])
order_router = make_CRUD(Order, types=[CRUD_types.LIST, CRUD_types.DETAILS])
order_router.auth = django_auth


@order_router.get("/{id}/process")
def process(request, id: int):
    order = get_object_or_404(Order, id=id)

    try:
        with transaction.atomic():
            order.process(request)
            order.save()
    except TransitionNotAllowed as e:
        raise HttpError(400, f"{e}")

    return {"success": True}


@order_router.get("/{id}/complete")
def complete(request, id: int):
    order = get_object_or_404(Order, id=id)

    try:
        with transaction.atomic():
            order.complete()
            order.save()
    except TransitionNotAllowed as e:
        raise HttpError(400, f"{e}")

    return {"success": True}


router = Router()
router.add_router("/product/", product_router)
router.add_router("/table/", table_router)
router.add_router("/order/", order_router)
