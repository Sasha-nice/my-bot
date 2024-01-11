from typing import Any

from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class BaseModel(Base):
    __abstract__ = True
