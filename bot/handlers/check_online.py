from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.filters.exception import ErrorEvent, ExceptionTypeFilter
from aiogram.types import Message

from bot.exceptions.exceptions import NoArgumentProvided
from controllers.check_online import CheckOnlineController
from utils.parse_vk_username import parse_vk_username

router = Router()


@router.message(Command("check_online"))
async def check_online_handler(
    msg: Message, command: CommandObject, check_online_controller: CheckOnlineController
) -> None:
    vk_id = parse_vk_username(command.args)
    user_info = await check_online_controller.check_online(vk_id)
    response = (
        "Online" if user_info.online else f"Not online since {user_info.last_seen.time}"
    )
    await msg.answer(response)


@router.error(ExceptionTypeFilter(NoArgumentProvided))
async def handle_no_arguments(event: ErrorEvent) -> None:
    if event.update.message:
        await event.update.message.answer("Need vk url")
