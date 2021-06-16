from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.orm import declarative_mixin, declared_attr


@declarative_mixin
class BaseClass:
    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    __table_args__ = {"mysql_engine": "InnoDB"}
    __mapper_args__ = {"always_refresh": True}

    id = Column(Integer, primary_key=True, index=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
