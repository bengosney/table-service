# Third Party
from ninja.orm import create_schema

# First Party
from products.models import Product

ProductSchema = create_schema(Product, exclude=Product._exclude)
ProductCreateSchema = create_schema(Product, name="ProductCreate", exclude=Product._exclude_create)
