from enum import Enum

import sqlalchemy
from sqlalchemy import Integer, Text
from sqlalchemy.dialects.postgresql import ENUM

from bot.storage.models.base import BaseModel


class Timezones(Enum):
    ZERO = "+0"
    ONE = "+1"
    TWO = "+2"
    THREE = "+3"


class Users(BaseModel):
    __tablename__ = "users"

    id = sqlalchemy.Column(Integer, nullable=False, unique=True, primary_key=True)
    name = sqlalchemy.Column(Text, nullable=True)
    timezone = sqlalchemy.Column(ENUM(Timezones), nullable=True, default=Timezones.ZERO)
