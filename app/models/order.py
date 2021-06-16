from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer

from app.database import Base
from app.models.mixins import BaseClass

order_link_product = Table(
    "order_link_product",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
)


class Order(Base, BaseClass):
    table_id = Column(Integer, ForeignKey("tables.id"))
    table = relationship(
        "Table",
    )

    products = relationship("Product", secondary=order_link_product)
