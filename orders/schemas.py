# First Party
from api.schema import make_schemas
from orders.models import Order

OrderSchema, OrderCreateSchema, OrderUpdateSchema = make_schemas(Order)
