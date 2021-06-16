from sqlalchemy import Boolean, Column, String

from app.database import Base
from app.models.mixins import BaseClass


class Product(Base, BaseClass):
    name = Column(String(255), index=True)
    inStock = Column(Boolean, default=True)
