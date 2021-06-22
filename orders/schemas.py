# First Party
from api.schema import make_schemas
from orders.models import Category, Order, Product, Table

OrderSchema, OrderCreateSchema, OrderUpdateSchema = make_schemas(Order)


ProductSchema, ProductCreateSchema, ProductUpdateSchema = make_schemas(Product, depth=1)
CategorySchema, CategoryCreateSchema, CategoryUpdateSchema = make_schemas(Category)


TableSchema, TableCreateSchema, TableUpdateSchema = make_schemas(Table)
