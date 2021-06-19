# First Party
from api.schema import make_schemas
from tables.models import Table

TableSchema, TableCreateSchema, TableUpdateSchema = make_schemas(Table)
