import typing as tp

import telegram


def get_message_content(update: telegram.Update) -> tp.Optional[str]:
    if not update.effective_message.text:
        return None

    tokens = update.effective_message.text.split()
    content = " ".join(tokens[1:])

    if not content:
        return None

    return content
