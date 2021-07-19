from __future__ import annotations

import dataclasses
import datetime
import typing as tp

import vk_api


@dataclasses.dataclass
class VKPost:
    id: int
    owner_id: int
    date: datetime.datetime
    text: str

    @classmethod
    def from_dict(cls, data: tp.Dict[str, tp.Union[int, str]]) -> VKPost:
        post_id = data["id"]
        post_owner_id = data["owner_id"]
        post_date = datetime.datetime.fromtimestamp(data["date"])
        post_text = data["text"]

        return cls(post_id, post_owner_id, post_date, post_text)


class VKPostScanner:
    DOMAIN_URL = "baraholkanastolok"

    def __init__(self, username: str, password: str):
        self._last_fetched_date = datetime.datetime.min
        self._session = vk_api.VkApi(username, password, auth_handler=self.auth_handle)
        self._session.auth()
        self._vk = self._session.get_api()

    @staticmethod
    def auth_handle() -> tp.Tuple[str, bool]:
        auth_code = input("Enter VK 2FA code: ")
        return auth_code, True

    def get_latest_posts(self) -> tp.List[VKPost]:
        wall_posts_raw = self._vk.wall.get(
            domain=self.DOMAIN_URL,
            count=50
        )["items"]

        wall_posts = [VKPost.from_dict(post_data) for post_data in wall_posts_raw]
        return wall_posts
