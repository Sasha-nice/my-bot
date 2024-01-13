import datetime

import sqlalchemy
from sqlalchemy import Integer, Interval, Text

from bot.storage.models.base import BaseModel


class Users(BaseModel):
    __tablename__ = "users"

    id = sqlalchemy.Column(Integer, nullable=False, unique=True, primary_key=True)
    name = sqlalchemy.Column(Text, nullable=True)
    timezone = sqlalchemy.Column(
        Interval, nullable=False, default=datetime.timedelta(hours=0)
    )
