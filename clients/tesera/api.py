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

    def get_game_by_alias(self, alias: str) -> model.BoardGame:
        data = self._get(f"games/{alias}")
        return model.BoardGame((data))

    def find_game_by_name(self, name: str) -> model.BoardGame:
        data = self._get("search/games", {
            "query": name
        })

        if not data:
            raise TeseraGameNotFoundError(f"No such game with the name {name}")

        alias = data[0]["alias"]
        return self.get_game_by_alias(alias)

    def generate_recommendation(self, names: tp.Iterable[str]) -> tp.Iterable[model.BoardGame]:
        games = list()
        similar_games = list()

        for name in names:
            try:
                games.append(self.find_game_by_name(name))
            except TeseraGameNotFoundError:
                continue

        for game in games:
            similar_games.append(set(similar_game.alias for similar_game in game.similar_games))
        filtered_games = set()

        for idx, titles in enumerate(similar_games):
            if idx == 0:
                filtered_games = titles
            else:
                filtered_games.intersection(titles)

        recommendation: tp.List[model.BoardGame] = list()
        # Too bad, no games were found
        if not filtered_games:
            for games in similar_games:
                for alias in games:
                    recommendation.append(self.get_game_by_alias(alias))
        else:
            recommendation: tp.List[model.BoardGame] = list(map(lambda x: self.get_game_by_alias(x), filtered_games))

        recommendation.sort(key=lambda x: x.info.rating, reverse=True)
        return recommendation[:5]
