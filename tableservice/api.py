# Third Party
from ninja import NinjaAPI

# First Party
from orders.api import router as order_router
from products.api import router as product_router
from tables.api import router as table_router

api = NinjaAPI(title="Table Service")

api.add_router("/products/", product_router)
api.add_router("/tables/", table_router)
api.add_router("/orders/", order_router)
