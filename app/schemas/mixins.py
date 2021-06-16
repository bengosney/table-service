import datetime

from pydantic import BaseModel


class BaseClass(BaseModel):
    id: int
    deleted: bool = False
    created_at: datetime.datetime
    updated_at: datetime.datetime
