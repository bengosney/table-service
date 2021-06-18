# Standard Library
from typing import List

# Third Party
from ninja import Router
from ninja.schema import Schema

# First Party
from tables.models import Table
from tables.schemas import TableCreateSchema, TableSchema
from tableservice.auth import AuthBearer

router = Router()


@router.get("/", response=List[TableSchema])
def list_tables(request) -> List[TableSchema]:
    return [i for i in Table.objects.all()]


@router.get("/{item_id}", response=TableSchema)
def table_details(request, item_id: int) -> TableSchema:
    return Table.objects.get(id=item_id)


@router.post("/", response=Schema, auth=AuthBearer())
def create_table(request, payload: TableCreateSchema):
    return Table.objects.create(**payload.dict())
