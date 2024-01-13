from aiogram.filters import CommandStart
from aiogram.types import Message, User

from bot.handlers.callbacks.start import router
from bot.handlers.keyboards.start import get_keyboard


@router.message(CommandStart())
async def start_handler(msg: Message) -> None:
    if isinstance(msg.from_user, User):
        await msg.answer(
            "Choose your timezone",
            reply_markup=get_keyboard(
                user_id=msg.from_user.id, user_name=msg.from_user.full_name
            ),
        )
