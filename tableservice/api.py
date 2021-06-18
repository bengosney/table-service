# Third Party
from ninja import NinjaAPI

# First Party
from service.api import router as services_router

api = NinjaAPI(title="Table Service")

api.add_router("/services/", services_router)
