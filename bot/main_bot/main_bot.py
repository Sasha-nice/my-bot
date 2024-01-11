from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from bot.clients.vk_client import VkClient
from bot.handlers.handlers import router
from bot.middlewares.dependencies import DependenciesMiddleware


class MainBot:
    def __init__(
        self,
        telegram_bot_token: str,
        vk_api_version: str,
        vk_api_token: str,
        vk_api_base_url: str,
    ):
        self.bot = Bot(token=telegram_bot_token, parse_mode=ParseMode.HTML)
        self._vk_client = VkClient(
            api_version=vk_api_version, token=vk_api_token, url=vk_api_base_url
        )
        self.dp = Dispatcher()
        self.dp.message.middleware(DependenciesMiddleware(self._vk_client))
        self.dp.include_router(router)

    async def start(self):
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(
            self.bot, allowed_updates=self.dp.resolve_used_update_types()
        )
