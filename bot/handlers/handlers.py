from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.filters.exception import ErrorEvent, ExceptionTypeFilter
from aiogram.types import Message

from bot.clients.vk_client import VkClient
from bot.exceptions.exceptions import NoArgumentProvided
from utils.parse_vk_username import parse_vk_username

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    await msg.answer("Start")


@router.message(Command("check_online"))
async def check_online_handler(
    msg: Message, command: CommandObject, vk_client: VkClient
) -> None:
    vk_id = parse_vk_username(command.args)
    is_online = await vk_client.check_online(vk_id)
    await msg.answer(f"{'Online' if is_online else 'Not online'}")


@router.error(ExceptionTypeFilter(NoArgumentProvided))
async def handle_no_arguments(event: ErrorEvent) -> None:
    if event.update.message:
        await event.update.message.answer("Need vk url")
