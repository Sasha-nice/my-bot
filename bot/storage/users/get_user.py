import datetime

from aiopg.sa import Engine
from sqlalchemy import select

from bot.storage.models.users import Users


async def get_tg_user_timezone(tg_user_id: int, engine: Engine) -> datetime.timedelta:
    query = select(Users.timezone).where(Users.id == tg_user_id)

    async with engine.acquire() as conn:
        cursor = await conn.execute(query)
        result = (await cursor.fetchone()).timezone

    return result
