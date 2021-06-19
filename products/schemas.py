# First Party
from api.schema import make_schemas
from products.models import Category, Product

ProductSchema, ProductCreateSchema, ProductUpdateSchema = make_schemas(Product, depth=1)
CategorySchema, CategoryCreateSchema, CategoryUpdateSchema = make_schemas(Category)
