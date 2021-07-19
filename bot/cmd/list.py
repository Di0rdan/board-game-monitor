import telegram.ext

from bot import base, constants
from bot.interface import message


class ListHandle(base.BaseHandle):

    def __init__(self):
        pass

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        if constants.DB_NAME not in context.user_data or not context.user_data[constants.DB_NAME]:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_NO_GAMES_TRACKED)
            return

        listings = []
        for game in context.user_data[constants.DB_NAME]:
            listings.append(f"— {game}")
        listings_msg = "\n".join(listings)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message.MSG_LIST_TRACKING_GAMES.format(len(listings), listings_msg)
        )

    @property
    def cmd_name(self) -> str:
        return "list"
