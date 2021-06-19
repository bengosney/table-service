# Third Party
from ninja.router import Router

# First Party
from api.api import make_CRUD
from products.models import Category, Product
from products.schemas import (
    CategoryCreateSchema,
    CategorySchema,
    CategoryUpdateSchema,
    ProductCreateSchema,
    ProductSchema,
    ProductUpdateSchema,
)

router = Router()

product_router = make_CRUD(Product, ProductSchema, ProductCreateSchema, ProductUpdateSchema)
category_router = make_CRUD(Category, CategorySchema, CategoryCreateSchema, CategoryUpdateSchema)

router.add_router("/product/", product_router)
router.add_router("/category/", category_router)
