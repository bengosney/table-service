# Third Party
from ninja.orm import create_schema

# First Party
from service.models import Order, Product, Table

ProductSchema = create_schema(Product, exclude=["deleted"])
ProductCreateSchema = create_schema(
    Product, name="ProductCreate", exclude=["deleted", "id", "position", "created", "last_updated"]
)

TableSchema = create_schema(Table, exclude=["deleted"])
TableCreateSchema = create_schema(
    Table, name="TableCreate", exclude=["deleted", "id", "position", "created", "last_updated"]
)

OrderSchema = create_schema(Order, exclude=["deleted"], depth=1)
OrderCreateSchema = create_schema(
    Order, name="OrderCreate", exclude=["deleted", "id", "position", "created", "last_updated"]
)
