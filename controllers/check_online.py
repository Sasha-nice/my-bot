from bot.clients.vk_client import VkClient


class CheckOnlineController:
    def __init__(self, vk_client: VkClient):
        self._vk_client = vk_client

    async def check_online(self, user_id: int | str):
        return await self._vk_client.check_online(user_id)
