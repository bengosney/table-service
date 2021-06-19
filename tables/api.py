# First Party
from api.api import make_CRUD
from tables.models import Table
from tableservice.auth import AuthBearer

router = make_CRUD(Table, write_auth=AuthBearer)
