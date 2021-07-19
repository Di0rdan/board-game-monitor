import typing as tp

import telegram.ext

from bot import base
from bot import utils
from bot import constants
from bot.interface import message


class DeleteHandle(base.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)

        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_INVALID_NAME)
            return

        if constants.DB_NAME not in context.user_data:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_NOT_FOUND)
            return

        if msg in context.user_data[constants.DB_NAME]:
            context.user_data[constants.DB_NAME].remove(msg)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message.MSG_GAME_DELETED_FROM_DB.format(msg)
            )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message.MSG_GAME_NOT_FOUND
            )

    @property
    def cmd_name(self) -> str:
        return "delete"
