import abc

import telegram.ext

__all__ = []


class BaseHandle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __call__(self, update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
        raise NotImplementedError("__call__ method should be implemented for BaseHandle descendant")

    @property
    @abc.abstractmethod
    def cmd_name(self) -> str:
        raise NotImplementedError(
            "__cmd method should be implemented and return the name of a command to handle"
        )


class TelegramBot:

    def __init__(self, auth_token: str):
        self.updater = telegram.ext.Updater(auth_token)
        self.dispatcher: telegram.ext.Dispatcher = self.updater.dispatcher

    def register_handlers(self):
        base_cls = BaseHandle
        lst = base_cls.__subclasses__()
        for cls in BaseHandle.__subclasses__():
            instance: BaseHandle = cls()
            self.dispatcher.add_handler(telegram.ext.CommandHandler(instance.cmd_name, instance))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()
