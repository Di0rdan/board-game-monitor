import telegram.ext

from bot import base
from bot.interface import message


class HelpHandle(base.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_HELP_LIST_COMMANDS)

    @property
    def cmd_name(self) -> str:
        return "help"
