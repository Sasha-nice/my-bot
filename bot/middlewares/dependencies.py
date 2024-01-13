from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiopg.sa.engine import create_engine

from bot.clients.vk_client import VkClient
from bot.controllers.check_online import CheckOnlineController
from bot.controllers.start import StartController


class DependenciesMiddleware(BaseMiddleware):
    def __init__(self, vk_client: VkClient, dsn: str) -> None:
        self._vk_client = vk_client
        self._dsn = dsn

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        engine = await create_engine(dsn=self._dsn)
        data["check_online_controller"] = CheckOnlineController(self._vk_client, engine)
        data["start_controller"] = StartController(engine)
        return await handler(event, data)
