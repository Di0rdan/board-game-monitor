import requests
import typing as tp


class DefaultTeseraClient:

    def __init__(self):
        self._session = requests.Session()
        self._bind_uri = "https://api.tesera.ru"

    def _get(self, endpoint: str, query: tp.Optional[dict] = None) -> dict:
        response = self._session.get(f"{self._bind_uri}/{endpoint}", params=query)
        response.raise_for_status()

        return response.json()

    def list_games(self):
        return self._get(f"games")

    def search_games(self, name: str):
        return self._get("search/games", {
            "query": name
        })
