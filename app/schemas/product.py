from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    inStock: bool = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
