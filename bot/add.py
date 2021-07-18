import typing as tp

import telegram.ext

import bot
from bot.interface import message
from bot import utils


class AddHandle(bot.BaseHandle):

    def __init__(self):
        self._storage: tp.Dict[str, str] = dict()

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)
        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_INVALID_NAME)
            return
        self._storage[update.effective_user.id] = msg
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_ADDED_TO_DB.format(msg))

    @property
    def cmd_name(self) -> str:
        return "add"
