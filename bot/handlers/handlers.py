from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.clients.vk_client import VkClient
from utils.parse_vk_username import parse_vk_username

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Start")


@router.message(Command("check_online"))
async def check_online_handler(
    msg: Message, command: CommandObject, vk_client: VkClient
):
    vk_id = parse_vk_username(command.args)
    is_online = await vk_client.check_online(vk_id)
    await msg.answer(f"{'Online' if is_online else 'Not online'}")
