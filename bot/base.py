import abc

import telegram.ext


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
