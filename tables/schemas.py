# Third Party
from ninja.orm import create_schema

# First Party
from tables.models import Table

TableSchema = create_schema(Table, exclude=Table._exclude)
TableCreateSchema = create_schema(Table, name="TableCreate", exclude=Table._exclude_create)
