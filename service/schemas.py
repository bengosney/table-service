# Third Party
from ninja.orm import create_schema

# First Party
from service.models import Product

base_product_excludes = ["deleted"]

ProductSchema = create_schema(Product, exclude=base_product_excludes)
ProductCreateSchema = create_schema(
    Product, exclude=base_product_excludes + ["id", "position", "created", "last_updated"]
)
