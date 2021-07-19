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
        self.dispatcher.add_handler(telegram.ext.MessageHandler(
            telegram.ext.filters.Filters.text,
            self._default_message_handle
        ))

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def _default_message_handle(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        if "recommend" in context.user_data:
            if context.user_data["recommend"] == cmd.recommend.RecommendHandleStatus.AWAITING_INPUT:
                cmd.recommend.generate_and_send_recommendation(update, context)
                context.user_data["recommend"] = cmd.recommend.RecommendHandleStatus.SLEEPING
