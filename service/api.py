# Standard Library
from typing import List

# Third Party
from ninja import Router

# First Party
from service.models import Product
from service.schemas import ProductCreateSchema, ProductSchema

router = Router()

product_router = Router()


@product_router.get("/", response=List[ProductSchema])
def list_products(request) -> List[Product]:
    return [p for p in Product.objects.all()]


@product_router.get("/{product_id}", response=ProductSchema)
def producut_details(request, product_id: int) -> Product:
    product = Product.objects.get(id=product_id)
    return product


@product_router.post("/", response=ProductSchema)
def create_product(request, payload: ProductCreateSchema):
    product = Product.objects.create(**payload.dict())
    return product


router.add_router("/products/", product_router)
