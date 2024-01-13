import datetime

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.handlers.callbacks.start import Action, StartCallback


def get_keyboard(user_id: int | str, user_name: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    for i in range(-12, 13):
        keyboard.button(
            text=f"utc {i}" if i <= 0 else f"utc +{i}",
            callback_data=StartCallback(
                user_id=user_id,
                user_name=user_name,
                timezone=datetime.timedelta(hours=i),
                action=Action.set_timezone,
            ),
        )
    keyboard.button(
        text="Skip",
        callback_data=StartCallback(
            user_id=user_id,
            user_name=user_name,
            action=Action.set_timezone,
        ),
    )
    keyboard.adjust(5)
    return keyboard.as_markup(one_time_keyboard=True)
