# Third Party
from ninja import Router

# First Party
from api.api import CRUD_types, make_CRUD
from api.schema import make_schemas, schema_types
from orders.models import Category, Order, Product, Table
from tableservice.auth import AuthBearer

product_router = make_CRUD(Product, write_auth=AuthBearer)
category_router = make_CRUD(Category, write_auth=AuthBearer)
table_router = make_CRUD(Table, write_auth=AuthBearer)

product_router.add_router("/category/", category_router)

make_schemas(Order, depth=2, types=[schema_types.FETCH])
order_router = make_CRUD(Order, read_auth=AuthBearer, types=[CRUD_types.LIST, CRUD_types.DETAILS])


@order_router.get("process")
def process(request, order_id: int):
    pass


@order_router.get("complete")
def complete(request, order_id: int):
    pass


router = Router()
router.add_router("/product/", product_router)
router.add_router("/table/", table_router)
router.add_router("/order/", order_router)
