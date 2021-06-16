from pydantic import BaseModel

from app.schemas.mixins import BaseClass


class ProductBase(BaseModel):
    name: str
    inStock: bool = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase, BaseClass):
    id: int

    class Config:
        orm_mode = True
