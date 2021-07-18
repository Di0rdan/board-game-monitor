import typing as tp

import telegram.ext

from bot.interface import message
from clients.tesera.model import BoardGame


def get_message_content(update: telegram.Update) -> tp.Optional[str]:
    if not update.effective_message.text:
        return None

    tokens = update.effective_message.text.split()
    content = " ".join(tokens[1:])

    if not content:
        return None

    return content


def split_strings_into_tokens(collection: str) -> tp.List[str]:
    words = collection.split()

    for idx, word in enumerate(words):
        cleaned_word = word.replace(",", "")
        if cleaned_word:
            words[idx] = cleaned_word

    return words


def send_info_about_game(game: BoardGame, update: telegram.Update, context: telegram.ext.CallbackContext):
    response = message.MSG_GAME_DESCRIPTION.format(
        game.info.title,
        game.info.rating,
        game.info.brief_description,
        game.info.players_count,
        game.info.players_count_recommended,
        game.info.url
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)
