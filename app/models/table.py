from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from app.database import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)

