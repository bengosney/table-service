# First Party
from api.api import CRUD_types, make_CRUD
from orders.models import Order
from tableservice.auth import AuthBearer

router = make_CRUD(Order, read_auth=AuthBearer, types=[CRUD_types.LIST, CRUD_types.DETAILS])
