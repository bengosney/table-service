from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
