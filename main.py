import asyncio
import logging

from bot.main_bot.main_bot import MainBot
from bot.settings import Config


async def main():
    bot = MainBot(
        telegram_bot_token=Config.TELEGRAM_TOKEN,
        vk_api_token=Config.VK_API_TOKEN,
        vk_api_version=Config.VK_API_VERSION,
        vk_api_base_url=Config.VK_API_BASE_URL,
        db_host=Config.DB_HOST,
        db_name=Config.DB_NAME,
        db_password=Config.DB_PASSWORD,
        db_port=Config.DB_PORT,
        db_user=Config.DB_USER,
    )
    await bot.start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
