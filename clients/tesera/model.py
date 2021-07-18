import typing as tp

URL = "https://api.tesera.ru"


class BoardGameInfo:

    def __init__(self, raw_data: tp.Dict[str, str]):
        self._raw_data = raw_data

    def to_json(self):
        return self._raw_data

    @property
    def name(self) -> str:
        return self._raw_data["alias"]

    @property
    def title(self) -> str:
        return self._raw_data["title"]

    @property
    def brief_description(self) -> str:
        return self._raw_data["descriptionShort"]

    @property
    def description(self) -> str:
        return self._raw_data["description"]

    @property
    def url(self) -> str:
        return self._raw_data["teseraUrl"]

    @property
    def rating(self):
        return self._raw_data["ratingUser"]

    @property
    def players_count(self):
        min_count = self._raw_data["playersMin"]
        max_count = self._raw_data["playersMax"]
        return f"{min_count}-{max_count}"

    @property
    def players_count_recommended(self):
        min_count = self._raw_data["playersMinRecommend"]
        max_count = self._raw_data["playersMaxRecommend"]
        return f"{min_count}-{max_count}"

