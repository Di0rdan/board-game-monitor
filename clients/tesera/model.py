import typing as tp

URL = "https://api.tesera.ru"
BoardGameDescription = tp.Dict[str, str]
BoardGameEntry = tp.Union[BoardGameDescription, tp.List[BoardGameDescription]]


class BoardGameInfo:

    def __init__(self, raw_data: BoardGameDescription):
        self._raw_data = raw_data

    def to_json(self):
        return self._raw_data

    @property
    def alias(self) -> str:
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


class BoardGame:

    def __init__(self, raw_data: tp.Dict[str, BoardGameEntry]):
        self._raw_data = raw_data

    def to_json(self):
        return self._raw_data

    @property
    def info(self) -> BoardGameInfo:
        return BoardGameInfo(self._raw_data["game"])

    @property
    def similar_games(self) -> tp.List[BoardGameInfo]:
        return [BoardGameInfo(data) for data in self._raw_data["similars"]]

