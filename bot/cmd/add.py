import telegram.ext
import typing as tp
from bot import base, utils, constants
from bot.interface import message


class AddHandle(base.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)
        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_INVALID_NAME)
            return

        if constants.DB_NAME not in context.user_data:
            context.user_data[constants.DB_NAME]: tp.Set[str] = set()

        if msg in context.user_data[constants.DB_NAME]:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_ALREADY_ADDED_TO_DB)
        else:
            context.user_data[constants.DB_NAME].add(msg)
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_ADDED_TO_DB.format(msg))

    @property
    def cmd_name(self) -> str:
        return "add"
