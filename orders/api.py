# Standard Library
from typing import List

# Third Party
from ninja import Router

# First Party
from orders.models import Order
from orders.schemas import OrderCreateSchema, OrderSchema
from tableservice.auth import AuthBearer

router = Router()


@router.get("/", response=List[OrderSchema], auth=AuthBearer())
def list_orders(request) -> List[Order]:
    return [p for p in Order.objects.all()]


@router.get("/{Order_id}", response=OrderSchema, auth=AuthBearer())
def order_details(request, Order_id: int) -> Order:
    return Order.objects.get(id=Order_id)


@router.post("/", response=OrderSchema, auth=AuthBearer())
def create_order(request, payload: OrderCreateSchema):
    return Order.objects.create(**payload.dict())
