import datetime

from aiopg.sa import Engine
from pydantic import BaseModel

from bot.clients.vk_client import VkClient
from bot.storage.users.get_user import get_tg_user_timezone


class CheckOnlineResult(BaseModel):
    is_online: bool
    last_seen: datetime.datetime | None


class CheckOnlineController:
    def __init__(self, vk_client: VkClient, engine: Engine):
        self._vk_client = vk_client
        self._engine = engine

    async def check_online(self, vk_user_id: int | str, tg_user_id: int):
        vk_user_info = await self._vk_client.check_online(vk_user_id)
        timezone = await get_tg_user_timezone(tg_user_id, self._engine)
        return CheckOnlineResult(
            is_online=vk_user_info.online,
            last_seen=vk_user_info.last_seen.time + timezone,
        )
