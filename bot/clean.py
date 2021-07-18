import telegram.ext

import bot
from bot.interface import message


class CleanHandle(bot.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_PLACEHOLDER)

    @property
    def cmd_name(self) -> str:
        return "clean"
