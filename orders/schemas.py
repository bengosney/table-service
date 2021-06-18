# Third Party
from ninja.orm import create_schema

# First Party
from orders.models import Order

OrderSchema = create_schema(Order, exclude=["deleted"], depth=1)
OrderCreateSchema = create_schema(
    Order, name="OrderCreate", exclude=["deleted", "id", "position", "created", "last_updated"]
)
