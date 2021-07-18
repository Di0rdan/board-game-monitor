import requests
from clients.tesera import model
import typing as tp


class TeseraClientError(Exception):
    pass


class TeseraGameNotFoundError(Exception):
    pass


class DefaultTeseraClient:

    def __init__(self):
        self._session = requests.Session()
        self._bind_uri = "https://api.tesera.ru"

    def _get(self, endpoint: str, query: tp.Optional[dict] = None) -> dict:
        response = self._session.get(f"{self._bind_uri}/{endpoint}", params=query)
        response.raise_for_status()

        return response.json()

    def find_game_by_name(self, name: str) -> model.BoardGameInfo:
        data = self._get("search/games", {
            "query": name
        })

        if not data:
            raise TeseraGameNotFoundError(f"No such game with the name {name}")

        alias = data[0]["alias"]
        data = self._get(f"games/{alias}")

        return model.BoardGameInfo(data["game"])
