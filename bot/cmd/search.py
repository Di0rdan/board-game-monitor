import telegram.ext

from bot import base, utils
from bot.interface import message
from clients.tesera import DefaultTeseraClient
from clients.tesera import TeseraGameNotFoundError


class SearchHandle(base.BaseHandle):

    def __init__(self):
        self._tesera_client = DefaultTeseraClient()

    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        msg = utils.get_message_content(update)

        if not msg:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_INVALID_NAME)
            return

        try:
            game = self._tesera_client.find_game_by_name(msg)
        except TeseraGameNotFoundError:
            context.bot.send_message(chat_id=update.effective_chat.id, text=message.MSG_GAME_NOT_FOUND)
            return

        response = message.MSG_GAME_DESCRIPTION.format(
            game.name,
            game.rating,
            game.brief_description,
            game.players_count,
            game.players_count_recommended,
            game.url
        )

        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    @property
    def cmd_name(self) -> str:
        return "search"
