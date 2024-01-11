import datetime
from collections.abc import Sequence
from typing import Any, Dict

from pydantic import BaseModel

from bot.clients.base_client import BaseClient


class SingleUser(BaseModel):
    class LastSeen(BaseModel):
        time: datetime.datetime

    online: bool
    last_seen: LastSeen


class VkUserResponse(BaseModel):
    response: Sequence[SingleUser]


class VkClient(BaseClient):
    def __init__(self, token: str, url: str, api_version: str):
        self.__token = token
        self.__api_version = api_version
        super().__init__(url)

    async def check_online(self, user_id: int | str) -> SingleUser:
        def _get_params() -> Dict[str, Any]:
            return {
                "user_ids": user_id,
                "v": self.__api_version,
                "fields": "online, last_seen, timezone",
            }

        response = await self.get(self._url + "users.get", params=_get_params())
        return VkUserResponse(**response).response[0]

    def _get_headers(self) -> Dict[str, Any]:
        return {"Authorization": self.__token}
