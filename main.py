import logging
import typing as tp

import telegram.bot
import telegram.ext

TOKEN = "1916132812:AAGLN-5c4Io_uXQOaRyy62SobDBD9zDC0zk"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

STORAGE = dict()


def get_message_content(update: telegram.Update) -> tp.Optional[str]:
    if not update.effective_message.text:
        return None

    tokens = update.effective_message.text.split()
    content = " ".join(tokens[1:])

    if not content:
        return None

    return content


def cmd_start(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def cmd_add(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    message = get_message_content(update)
    if not message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You must enter a valid name for a game!")
        return
    STORAGE[update.effective_user.id] = message
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added the game {message} to the database.")


def cmd_clean(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for clean command!")


def cmd_search(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    message = get_message_content(update)

    if not message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You must enter a valid name for a game!")
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You've entered: {message}")


def cmd_list(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for list command!")


def cmd_delete(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    message = get_message_content(update)

    if not message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You must enter a valid name for a game!")
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You've entered: {message}")
    if update.effective_user.id in STORAGE:
        del STORAGE[update.effective_user.id]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Deleted an entry for the game {message}.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Could not find such game in the database.")


def main():
    updater = telegram.ext.Updater(TOKEN)
    dispatcher: telegram.ext.Dispatcher = updater.dispatcher
    handlers = [
        telegram.ext.CommandHandler('start', cmd_start),
        telegram.ext.CommandHandler('add', cmd_add),
        telegram.ext.CommandHandler('search', cmd_search),
        telegram.ext.CommandHandler('delete', cmd_delete)
    ]

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
