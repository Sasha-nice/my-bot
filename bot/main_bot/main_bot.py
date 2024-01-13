from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import BotCommand

from bot.clients.vk_client import VkClient
from bot.handlers.check_online import router as handlers_router
from bot.handlers.start import router as start_router
from bot.middlewares.dependencies import DependenciesMiddleware


class MainBot:
    def __init__(
        self,
        telegram_bot_token: str,
        vk_api_version: str,
        vk_api_token: str,
        vk_api_base_url: str,
        db_user: str,
        db_host: str,
        db_port: int,
        db_password: str,
        db_name: str,
    ):
        self.bot = Bot(token=telegram_bot_token, parse_mode=ParseMode.HTML)
        self._vk_client = VkClient(
            api_version=vk_api_version, token=vk_api_token, url=vk_api_base_url
        )
        self.dp = Dispatcher()
        self.dp.message.middleware(
            DependenciesMiddleware(
                vk_client=self._vk_client,
                dsn=f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            )
        )
        self.dp.callback_query.middleware(
            DependenciesMiddleware(
                vk_client=self._vk_client,
                dsn=f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            )
        )
        self.dp.include_router(handlers_router)
        self.dp.include_router(start_router)

    async def _setup_commands(self) -> None:
        bot_commands = [
            BotCommand(command="/check_online", description="Checks if user is online"),
        ]
        await self.bot.set_my_commands(bot_commands)

    async def start(self) -> None:
        await self._setup_commands()
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(
            self.bot, allowed_updates=self.dp.resolve_used_update_types()
        )
