from typing import Optional

from aiogram import Router
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.clients.vk_client import VkClient
from bot.exceptions.exceptions import NoArgumentProvided
from utils.parse_vk_username import parse_vk_username


router = Router()

@router.error(ExceptionTypeFilter(NoArgumentProvided))
async def handle_no_arguments(msg: Message) -> None:
    await msg.answer("Need vk url")




