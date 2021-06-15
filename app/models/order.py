from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from app.database import Base
from .mixins import BaseClass

class Order(Base, BaseClass):
    pass