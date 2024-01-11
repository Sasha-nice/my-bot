from typing import Any, Dict

from aiohttp import ClientSession


class BaseClient:
    def __init__(self, url: str):
        self._url: str = url

    async def get(self, url: str, **kwargs: Any) -> Any:
        async with ClientSession() as session:
            kwargs["headers"] = self._get_headers()
            async with session.get(url=url, **kwargs) as response:
                return await response.json()

    def _get_headers(self) -> Dict[str, Any]:
        """Метод предназначен для использование в отнаследованных классах,
         которым нужны дополнительные заголовки(например авторизация)"""
        return {}
