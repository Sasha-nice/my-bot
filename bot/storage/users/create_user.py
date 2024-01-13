import datetime
from typing import Any, Dict

from aiopg.sa import Engine
from sqlalchemy.dialects.postgresql import insert

from bot.storage.models.users import Users


async def create_user(
    user_id: int, user_name: str, timezone: datetime.timedelta, engine: Engine
) -> None:
    query = (
        insert(Users)
        .values(**_validate_args(user_id, user_name, timezone))
        .on_conflict_do_nothing(index_elements=[Users.id])
        .returning(Users.id)
    )

    async with engine.acquire() as conn:
        await conn.scalar(query)


def _validate_args(
    user_id: int, user_name: str, timezone: datetime.timedelta
) -> Dict[str, Any]:
    if timezone:
        return dict(id=user_id, name=user_name, timezone=timezone)
    else:
        return dict(id=user_id, name=user_name)
