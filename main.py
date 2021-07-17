import logging

import telegram.bot
import telegram.ext

TOKEN = "1916132812:AAGLN-5c4Io_uXQOaRyy62SobDBD9zDC0zk"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def cmd_start(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def cmd_add(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for add command!")


def cmd_clean(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for clean command!")


def cmd_search(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    if not update.effective_message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Could not parse your input!")
        return

    tokens = update.effective_message.text.split()
    request_name = " ".join(tokens[1:])

    if not request_name:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You must enter the valid name of a game!")
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You've entered: {request_name}")


def cmd_list(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for list command!")


def cmd_delete(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="The placeholder for delete command!")


def main():
    updater = telegram.ext.Updater(TOKEN)
    dispatcher: telegram.ext.Dispatcher = updater.dispatcher

    start_handler = telegram.ext.CommandHandler('start', cmd_start)
    add_handler = telegram.ext.CommandHandler('add', cmd_add)
    search_handler = telegram.ext.CommandHandler('search', cmd_search)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(add_handler)
    dispatcher.add_handler(search_handler)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
