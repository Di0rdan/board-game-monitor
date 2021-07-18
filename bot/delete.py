import typing as tp

import telegram.ext

import bot
from bot.interface import message
from bot import utils


class DeleteHandle(bot.BaseHandle):

    def __init__(self):
        self._storage: tp.Dict[str, str] = dict()

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)

        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_INVALID_NAME)
            return

        if update.effective_user.id in self._storage:
            del self._storage[update.effective_user.id]
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
