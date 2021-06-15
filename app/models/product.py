from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from app.database import Base
from .mixins import BaseClass

class Product(Base, BaseClass):
    name = Column(String(255), index=True)
    inStock = Column(Boolean, default=True)

    deleted = Column(Boolean, default=False)
    