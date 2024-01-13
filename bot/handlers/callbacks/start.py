import datetime
from enum import Enum

from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message

from controllers.start import StartController


class Action(str, Enum):
    set_timezone = "set_timezone"


class StartCallback(CallbackData, prefix="start"):
    action: Action
    user_id: int | str
    user_name: str
    timezone: datetime.timedelta | None = None


router = Router()


@router.callback_query(StartCallback.filter(F.action == Action.set_timezone))
async def handle_callback_timezone(
    callback: CallbackQuery,
    callback_data: StartCallback,
    start_controller: StartController,
) -> None:
    await start_controller.register_user(
        user_id=callback_data.user_id,
        user_name=callback_data.user_name,
        user_timezone=callback_data.timezone,
    )
    if isinstance(callback.message, Message):
        await callback.message.edit_reply_markup()
        await callback.message.edit_text("Thanks")
