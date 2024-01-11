
from aiogram import Router
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types import Message

from bot.exceptions.exceptions import NoArgumentProvided

router = Router()


@router.error(ExceptionTypeFilter(NoArgumentProvided))
async def handle_no_arguments(msg: Message) -> None:
    await msg.answer("Need vk url")
