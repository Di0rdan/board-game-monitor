import telegram.ext

from bot import base, cmd, utils

__all__ = ["base", "cmd", "TelegramBot", "utils"]


class TelegramBot:

    def __init__(self, auth_token: str):
        self.updater = telegram.ext.Updater(auth_token)
        self.dispatcher: telegram.ext.Dispatcher = self.updater.dispatcher

    def register_handlers(self) -> None:
        for cls in base.BaseHandle.__subclasses__():
            instance: base.BaseHandle = cls()
            self.dispatcher.add_handler(telegram.ext.CommandHandler(instance.cmd_name, instance))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()
