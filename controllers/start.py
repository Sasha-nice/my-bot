import datetime

from aiopg.sa import Engine

from bot.storage.users.create_user import create_user


class StartController:
    def __init__(self, engine: Engine):
        self._engine = engine

    async def register_user(
        self,
        user_id: int | str,
        user_name: str,
        user_timezone: datetime.timedelta | None,
    ):
        await create_user(
            user_id=user_id,
            user_name=user_name,
            timezone=user_timezone,
            engine=self._engine,
        )
