from pydantic import BaseModel

from bot.clients.base_client import BaseClient


class VkUserResponse(BaseModel):
    online: bool


class VkClient(BaseClient):
    def __init__(self, token: str, url: str, api_version: str):
        self.__token = token
        self.__api_version = api_version
        super().__init__(url)

    async def check_online(self, user_id: int | str):
        def _get_params():
            return {"user_ids": user_id, "v": self.__api_version, "fields": "online"}

        response = await self.get(self._url + "users.get", params=_get_params())
        return response["response"][0]["online"]

    def _get_headers(self):
        return {"Authorization": self.__token}
