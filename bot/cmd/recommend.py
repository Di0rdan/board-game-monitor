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
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)

        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_AWAITING_USER_INPUT)
            context.user_data[self.cmd_name] = RecommendHandleStatus.AWAITING_INPUT
            return

        generate_and_send_recommendation(update, context)
        context.user_data[self.cmd_name] = RecommendHandleStatus.SLEEPING

    @property
    def cmd_name(self) -> str:
        return "recommend"


def generate_and_send_recommendation(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    client = DefaultTeseraClient()
    names = utils.split_strings_into_tokens(update.effective_message.text)
    recommendation = client.generate_recommendation(names)

    if recommendation:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message.MSG_FOUND_N_GAMES.format(len(recommendation))
        )
        for game in recommendation:
            utils.send_info_about_game(game, update, context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_RECOMMENDATION_NOT_GENERATED)
