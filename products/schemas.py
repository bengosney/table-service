# Third Party

# First Party
from api.schema import make_schemas
from products.models import Category, Product

ProductSchema, ProductCreateSchema, ProductUpdateSchema = make_schemas(Product, depth=1)
# ProductSchema = create_schema(Product, depth=1, exclude=Product._exclude)
# ProductCreateSchema = create_schema(Product, name="Product Create", exclude=Product._exclude_create)
# ProductUpdateSchema = create_schema(Product, name="Product Update", exclude=Product._exclude_create)

CategorySchema, CategoryCreateSchema, CategoryUpdateSchema = make_schemas(Category)
# CategorySchema = create_schema(Category, exclude=Category._exclude)
# CategoryCreateSchema = create_schema(Category, name="Category Create", exclude=Category._exclude_create)
