from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class DependenciesMiddleware(BaseMiddleware):
    def __init__(self, vk_client):
        self._vk_client = vk_client

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ):
        data["vk_client"] = self._vk_client
        return await handler(event, data)
