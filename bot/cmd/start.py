import telegram.ext

from bot import base
from bot.interface import message


class StartHandle(base.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_START_INFO)

    @property
    def cmd_name(self) -> str:
        return "start"
