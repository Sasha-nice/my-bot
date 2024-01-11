from aiohttp import ClientSession


class BaseClient:
    def __init__(self, url: str):
        self._url = url

    async def get(self, url: str, **kwargs):
        async with ClientSession() as session:
            kwargs["headers"] = self._get_headers()
            async with session.get(url, **kwargs) as response:
                return await response.json()

    def _get_headers(self):
        """Метод предназначен для использование в отнаследованных классах,
         которым нужны дополнительные заголовки(например авторизация)"""
        return {}
