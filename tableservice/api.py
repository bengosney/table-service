# Third Party
from ninja import NinjaAPI

# First Party
from orders.api import router as order_router

api = NinjaAPI(title="Table Service")

api.add_router("/", order_router)
