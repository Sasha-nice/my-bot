from bot.exceptions.exceptions import NoArgumentProvided


def parse_vk_username(vk_url: str | None) -> str:
    if not vk_url:
        raise NoArgumentProvided
    return vk_url.split("/")[-1]
