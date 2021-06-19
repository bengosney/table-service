# First Party
from api.api import CRUD_types, make_CRUD
from api.schema import make_schemas, schema_types
from orders.models import Order
from tableservice.auth import AuthBearer

make_schemas(Order, depth=2, types=[schema_types.FETCH])

router = make_CRUD(Order, read_auth=AuthBearer, types=[CRUD_types.LIST, CRUD_types.DETAILS])
