import enum

import telegram.ext

from bot import base, utils
from bot.interface import message
from clients.tesera import DefaultTeseraClient


class RecommendHandleStatus(enum.Enum):
    AWAITING_INPUT = "awaiting_input"
    SLEEPING = "sleeping"


class RecommendHandle(base.BaseHandle):

    def __init__(self):
        self._tesera_client = DefaultTeseraClient()

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)

        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_PLACEHOLDER)
            context.user_data[self.cmd_name] = RecommendHandleStatus.AWAITING_INPUT
            return

        names = utils.split_strings_into_tokens(update.effective_message.text)
        recommendation = self._tesera_client.generate_recommendation(names)

        if recommendation:
            for game in recommendation:
                utils.send_info_about_game(game, update, context)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_PLACEHOLDER)
        context.user_data[self.cmd_name] = RecommendHandleStatus.SLEEPING

    @property
    def cmd_name(self) -> str:
        return "recommend"
