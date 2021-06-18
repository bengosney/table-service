# Standard Library
from typing import List

# Third Party
from ninja import Router

# First Party
from products.models import Product
from products.schemas import ProductCreateSchema, ProductSchema
from tableservice.auth import AuthBearer

router = Router()


@router.get("/", response=List[ProductSchema])
def list_products(request) -> List[Product]:
    return [p for p in Product.objects.all()]


@router.get("/{product_id}", response=ProductSchema)
def product_details(request, product_id: int) -> Product:
    return Product.objects.get(id=product_id)


@router.post("/", response=ProductSchema, auth=AuthBearer())
def create_product(request, payload: ProductCreateSchema):
    return Product.objects.create(**payload.dict())
