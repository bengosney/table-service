# Standard Library
from typing import List

# Third Party
from ninja import Router
from ninja.security import HttpBearer

# First Party
from service.models import Product
from service.schemas import ProductCreateSchema, ProductSchema

router = Router()

product_router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


@product_router.get("/", response=List[ProductSchema])
def list_products(request) -> List[Product]:
    return [p for p in Product.objects.all()]


@product_router.get("/{product_id}", response=ProductSchema)
def producut_details(request, product_id: int) -> Product:
    return Product.objects.get(id=product_id)


@product_router.post("/", response=ProductSchema, auth=AuthBearer())
def create_product(request, payload: ProductCreateSchema):
    return Product.objects.create(**payload.dict())


router.add_router("/products/", product_router)
