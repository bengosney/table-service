# Third Party

# First Party
from api.api import make_CRUD
from products.models import Category, Product
from tableservice.auth import AuthBearer

router = make_CRUD(Product, write_auth=AuthBearer)
category_router = make_CRUD(Category, write_auth=AuthBearer)

router.add_router("/category/", category_router)
